# SinaNewsCatch

## 真实情况系微博登录流程
文件 ： loginLayer.js


### 加密用户名 

urlencode(d) -> sinaSSOEncoder.base64
 
```ecmascript 6
this.prelogin = function (a, b) {
    var c = ssoPreLoginUrl, d = a.username || "";
    d = sinaSSOEncoder.base64.encode(urlencode(d));
    delete a.username;
    var e = {entry: me.entry, callback: me.name + ".preloginCallBack", su: d, rsakt: "mod"};
    c = makeURL(c, objMerge(e, a));
    me.preloginCallBack = function (a) {
        if (a && a.retcode == 0) {
            me.setServerTime(a.servertime);
            me.nonce = a.nonce;
            me.rsaPubkey = a.pubkey;
            me.rsakv = a.rsakv;
            pcid = a.pcid;
            preloginTime = (new Date).getTime() - preloginTimeStart - (parseInt(a.exectime, 10) || 0)
        }
        typeof b == "function" && b(a)
    };
    preloginTimeStart = (new Date).getTime();
    excuteScript(me.scriptId, c)
};
```
### 密码

login -> loginMethodCheck -> loginByConfig -> loginByXMLHttpRequest -> prelogin

```ecmascript 6
customLogin = function (a) {
    a = a || {};
    customPrepare(a);
    me.login(e.username, e.password, e.savestate)
};

// a -> e.username b -> e.password c->e.savestate
this.login = function (a, b, c) {
    var d = arguments[3] ? arguments[3] : !1;
    if (getType(arguments[0]) === "object") return customLogin(arguments[0]);
    ssoLoginTimer ? ssoLoginTimer.clear() : ssoLoginTimer = new prototypeTimer(me.timeoutEnable);
    ssoLoginTimer.start(me.loginTimeout, function () {
        ssoLoginTimer.clear();
        me.callbackLoginStatus({
            result: !1,
            errno: -1,
            reason: unescape("%u767B%u5F55%u8D85%u65F6%uFF0C%u8BF7%u91CD%u8BD5")
        })
    });
    c = c == undefined ? 0 : c;
    tmpData.savestate = c;
    loginByConfig = function () {
        if (!me.feedBackUrl && loginByXMLHttpRequest(a, b, c, d)) return !0;
        if (me.useIframe && (me.setDomain || me.feedBackUrl)) {
            if (me.setDomain) {
                document.domain = me.domain;
                !me.feedBackUrl && me.domain != "sina.com.cn" && (me.feedBackUrl = makeURL(me.appLoginURL[me.domain], {domain: 1}))
            }
            loginMethod = "post";
            var e = loginByIframe(a, b, c, d);
            if (!e) {
                loginMethod = "get";
                me.scriptLoginHttps ? me.setLoginType(me.loginType | https) : me.setLoginType(me.loginType | rsa);
                loginByScript(a, b, c, d)
            }
        } else {
            loginMethod = "get";
            loginByScript(a, b, c, d)
        }
        me.nonce = null
    };
    loginMethodCheck = function () {
        if (me.loginType & wsse || me.loginType & rsa) {
            if (me.servertime) {
                me.nonce || (me.nonce = makeNonce(6));
                loginByConfig();
                return !0
            }
            me.getServerTime(a, loginByConfig)
        } else loginByConfig()
    };
    loginMethodCheck();
    return !0
};


loginByXMLHttpRequest = function (a, b, c, d) {
    if (typeof XMLHttpRequest == "undefined") return !1;
    var e = new XMLHttpRequest;
    if (!1 in e) return !1;
    var f = makeXMLRequestQuery(a, b, c, d),
        g = makeURL(ssoLoginUrl, {client: me.getClientType(), _: (new Date).getTime()});
    try {
        e.open("POST", g, !0);
        e.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        e.withCredentials = !0;
        e.onreadystatechange = function () {
            e.readyState == 4 && e.status == 200 && me.loginCallBack(parseJSON(e.responseText))
        };
        e.send(httpBuildQuery(f))
    } catch (h) {
        return !1
    }
    return !0
}
makeXMLRequestQuery = function (a, b, c, d) {
    if (me.appLoginURL[me.domain]) {
        me.useTicket = 1;
        me.service = me.appDomainService[me.domain] || me.service
    }
    var e = 0;
    me.domain && (e = 2);
    me.appLoginURL[me.domain] || (e = 3);
    me.cdult !== !1 && (e = me.cdult);
    if (e == 3) {
        crossDomainTime = me.crossDomainTime;
        delete me.appLoginURL[me.domain]
    }
    var f = makeRequest(a, b, c, d);
    return objMerge(f, {
        encoding: "UTF-8",
        cdult: e,
        domain: me.domain,
        useticket: me.appLoginURL[me.domain] ? 1 : 0,
        prelt: preloginTime,
        returntype: "TEXT"
    })
}
makeRequest = function (a, b, c, d) {
    var e = {
        entry: me.getEntry(),
        gateway: 1,
        from: me.from,
        savestate: c,
        qrcode_flag: d,
        useticket: me.useTicket ? 1 : 0
    };
    me.failRedirect && (me.loginExtraQuery.frd = 1);
    e = objMerge(e, {pagerefer: document.referrer || ""});
    e = objMerge(e, me.loginExtraFlag);
    e = objMerge(e, me.loginExtraQuery);
    e.su = sinaSSOEncoder.base64.encode(urlencode(a));
    me.service && (e.service = me.service);
    if (me.loginType & rsa && me.servertime && sinaSSOEncoder && sinaSSOEncoder.RSAKey) {
        e.servertime = me.servertime;
        e.nonce = me.nonce;
        e.pwencode = "rsa2";
        e.rsakv = me.rsakv;
        var f = new sinaSSOEncoder.RSAKey;
        f.setPublic(me.rsaPubkey, "10001");
        b = f.encrypt([me.servertime, me.nonce].join("\t") + "\n" + b)
    } else if (me.loginType & wsse && me.servertime && sinaSSOEncoder && sinaSSOEncoder.hex_sha1) {
        e.servertime = me.servertime;
        e.nonce = me.nonce;
        e.pwencode = "wsse";
        b = sinaSSOEncoder.hex_sha1("" + sinaSSOEncoder.hex_sha1(sinaSSOEncoder.hex_sha1(b)) + me.servertime + me.nonce)
    }
    e.sp = b;
    try {
        e.sr = window.screen.width + "*" + window.screen.height
    } catch (g) {
    }
    return e
}
```