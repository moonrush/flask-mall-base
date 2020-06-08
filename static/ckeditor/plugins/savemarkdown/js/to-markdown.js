﻿(function(y){"object"===typeof exports&&"undefined"!==typeof module?module.exports=y():"function"===typeof define&&define.amd?define([],y):("undefined"!==typeof window?window:"undefined"!==typeof global?global:"undefined"!==typeof self?self:this).toMarkdown=y()})(function(){return function e(f,h,a){function c(b,p){if(!h[b]){if(!f[b]){var g="function"==typeof require&&require;if(!p&&g)return g(b,!0);if(d)return d(b,!0);g=Error("Cannot find module '"+b+"'");throw g.code="MODULE_NOT_FOUND",g;}g=h[b]=
{exports:{}};f[b][0].call(g.exports,function(a){var d=f[b][1][a];return c(d?d:a)},g,g.exports,e,f,h,a)}return h[b].exports}for(var d="function"==typeof require&&require,b=0;b<a.length;b++)c(a[b]);return c}({1:[function(e,f,h){function a(a){return a.replace(/^[ \r\n\t]+|[ \r\n\t]+$/g,"")}function c(a){return-1!==B.indexOf(a.nodeName.toLowerCase())}function d(a){return-1!==C.indexOf(a.nodeName.toLowerCase())}function b(){var a=function(){};a.prototype.parseFromString=function(a){var d=w.implementation.createHTMLDocument("");
-1<a.toLowerCase().indexOf("\x3c!doctype")?d.documentElement.innerHTML=a:d.body.innerHTML=a;return d};return a}function r(a){for(var d="",b=0;b<a.childNodes.length;b++)1===a.childNodes[b].nodeType?d+=a.childNodes[b]._replacement:3===a.childNodes[b].nodeType&&(d+=a.childNodes[b].data);return d}function p(a,d){var b,g,p;"left"===a?(b=d.previousSibling,g=/ $/):(b=d.nextSibling,g=/^ /);b&&(3===b.nodeType?p=g.test(b.nodeValue):1!==b.nodeType||c(b)||(p=g.test(b.textContent)));return p}var g,u,A=e("./lib/md-converters"),
D=e("./lib/gfm-converters"),k=e("collapse-whitespace"),l="undefined"!==typeof window?window:this,w;w="undefined"===typeof document?e("jsdom").jsdom():document;var B="address article aside audio blockquote body canvas center dd dir div dl dt fieldset figcaption figure footer form frameset h1 h2 h3 h4 h5 h6 header hgroup hr html isindex li main menu nav noframes noscript ol output p pre section table tbody td tfoot th thead tr ul".split(" "),C="area base br col command embed hr img input keygen link meta param source track wbr".split(" "),
E=function(){var a=l.DOMParser,d=!1;try{(new a).parseFromString("","text/html")&&(d=!0)}catch(b){}return d}()?l.DOMParser:b();g=function(b,f){var e,h;f=f||{};if("string"!==typeof b)throw new TypeError(b+" is not a string");var l=b=b.replace(/(\d+)\. /g,"$1\\. "),l=(new E).parseFromString(l,"text/html");k(l,c);for(var l=l.body,v=[l],x=[],m,q;0<v.length;)for(m=v.shift(),x.push(m),m=m.childNodes,q=0;q<m.length;q++)1===m[q].nodeType&&v.push(m[q]);x.shift();u=A.slice(0);f.gfm&&(u=D.concat(u));f.converters&&
(u=f.converters.concat(u));for(v=x.length-1;0<=v;v--)if(m=x[v],h=void 0,q=r(m),d(m)||/A/.test(m.nodeName)||!/^\s*$/i.test(q)){for(e=0;e<u.length;e++){var z=u[e],n;n=m;var t=z.filter;if("string"===typeof t)n=t===n.nodeName.toLowerCase();else if(Array.isArray(t))n=-1!==t.indexOf(n.nodeName.toLowerCase());else if("function"===typeof t)n=t.call(g,n);else throw new TypeError("`filter` needs to be a string, array, or function");if(n){if("function"!==typeof z.replacement)throw new TypeError("`replacement` needs to be a function that returns a string");
e=m;h=n="";if(!c(e)){var t=/^[ \r\n\t]/.test(e.innerHTML),w=/[ \r\n\t]$/.test(e.innerHTML);t&&!p("left",e)&&(n=" ");w&&!p("right",e)&&(h=" ")}if((e=n)||h)q=a(q);h=e+z.replacement.call(g,q,m)+h;break}}m._replacement=h}else m._replacement="";return r(l).replace(/^[\t\r\n]+|[\t\r\n\s]+$/g,"").replace(/\n\s+\n/g,"\n\n").replace(/\n{3,}/g,"\n\n")};g.isBlock=c;g.isVoid=d;g.trim=a;g.outer=function(a,d){return a.cloneNode(!1).outerHTML.replace("\x3e\x3c","\x3e"+d+"\x3c")};f.exports=g},{"./lib/gfm-converters":2,
"./lib/md-converters":3,"collapse-whitespace":4,jsdom:7}],2:[function(e,f,h){function a(a,b){var c=" ";0===Array.prototype.indexOf.call(b.parentNode.childNodes,b)&&(c="| ");return c+a+" |"}var c=/highlight highlight-(\S+)/;f.exports=[{filter:"br",replacement:function(){return"\n"}},{filter:["del","s","strike"],replacement:function(a){return"~~"+a+"~~"}},{filter:function(a){return"checkbox"===a.type&&"LI"===a.parentNode.nodeName},replacement:function(a,b){return(b.checked?"[x]":"[ ]")+" "}},{filter:["th",
"td"],replacement:function(d,b){return a(d,b)}},{filter:"tr",replacement:function(d,b){var c="",p={left:":--",right:"--:",center:":-:"};if("THEAD"===b.parentNode.nodeName)for(var g=0;g<b.childNodes.length;g++){var e=b.childNodes[g].attributes.align,f="---";e&&(f=p[e.value]||f);c+=a(f,b.childNodes[g])}return"\n"+d+(c?"\n"+c:"")}},{filter:"table",replacement:function(a){return"\n\n"+a+"\n\n"}},{filter:["thead","tbody","tfoot"],replacement:function(a){return a}},{filter:function(a){return"PRE"===a.nodeName&&
a.firstChild&&"CODE"===a.firstChild.nodeName},replacement:function(a,b){return"\n\n```\n"+b.firstChild.textContent+"\n```\n\n"}},{filter:function(a){return"PRE"===a.nodeName&&"DIV"===a.parentNode.nodeName&&c.test(a.parentNode.className)},replacement:function(a,b){return"\n\n```"+b.parentNode.className.match(c)[1]+"\n"+b.textContent+"\n```\n\n"}},{filter:function(a){return"DIV"===a.nodeName&&c.test(a.className)},replacement:function(a){return"\n\n"+a+"\n\n"}}]},{}],3:[function(e,f,h){f.exports=[{filter:"p",
replacement:function(a){return"\n\n"+a+"\n\n"}},{filter:"br",replacement:function(){return"  \n"}},{filter:"h1 h2 h3 h4 h5 h6".split(" "),replacement:function(a,c){for(var d=c.nodeName.charAt(1),b="",e=0;e<d;e++)b+="#";return"\n\n"+b+" "+a+"\n\n"}},{filter:"hr",replacement:function(){return"\n\n* * *\n\n"}},{filter:["em","i"],replacement:function(a){return"_"+a+"_"}},{filter:["strong","b"],replacement:function(a){return"**"+a+"**"}},{filter:function(a){var c=a.previousSibling||a.nextSibling,c="PRE"===
a.parentNode.nodeName&&!c;return"CODE"===a.nodeName&&!c},replacement:function(a){return"`"+a+"`"}},{filter:function(a){return"A"===a.nodeName&&a.getAttribute("href")},replacement:function(a,c){var d=c.title?' "'+c.title+'"':"";return"["+a+"]("+c.getAttribute("href")+d+")"}},{filter:"img",replacement:function(a,c){var d=c.alt||"",b=c.getAttribute("src")||"",e=c.title||"";return b?"!["+d+"]("+b+(e?' "'+e+'"':"")+")":""}},{filter:function(a){return"PRE"===a.nodeName&&"CODE"===a.firstChild.nodeName},
replacement:function(a,c){return"\n\n    "+c.firstChild.textContent.replace(/\n/g,"\n    ")+"\n\n"}},{filter:"blockquote",replacement:function(a){a=this.trim(a);a=a.replace(/\n{3,}/g,"\n\n");a=a.replace(/^/gm,"\x3e ");return"\n\n"+a+"\n\n"}},{filter:"li",replacement:function(a,c){a=a.replace(/^\s+/,"").replace(/\n/gm,"\n    ");var d="*   ",d=c.parentNode,b=Array.prototype.indexOf.call(d.children,c)+1,d=/ol/i.test(d.nodeName)?b+".  ":"*   ";return d+a}},{filter:["ul","ol"],replacement:function(a,c){for(var d=
[],b=0;b<c.childNodes.length;b++)d.push(c.childNodes[b]._replacement);return/li/i.test(c.parentNode.nodeName)?"\n"+d.join("\n"):"\n\n"+d.join("\n")+"\n\n"}},{filter:function(a){return this.isBlock(a)},replacement:function(a,c){return"\n\n"+this.outer(c,a)+"\n\n"}},{filter:function(){return!0},replacement:function(a,c){return this.outer(c,a)}}]},{}],4:[function(e,f,h){function a(a){return!(!a||!r[a.nodeName])}function c(a){var b=a.nextSibling||a.parentNode;a.parentNode.removeChild(a);return b}function d(a,
b){return a&&a.parentNode===b||"PRE"===b.nodeName?b.nextSibling||b.parentNode:b.firstChild||b.nextSibling||b.parentNode}var b=e("void-elements");Object.keys(b).forEach(function(a){b[a.toUpperCase()]=1});var r={};e("block-elements").forEach(function(a){r[a.toUpperCase()]=1});f.exports=function(e,g){if(e.firstChild&&"PRE"!==e.nodeName){"function"!==typeof g&&(g=a);for(var f=null,h=!1,r=null,k=d(r,e);k!==e;){if(3===k.nodeType){var l=k.data.replace(/[ \r\n\t]+/g," ");f&&!/ $/.test(f.data)||h||" "!==l[0]||
(l=l.substr(1));if(!l){k=c(k);continue}k.data=l;f=k}else if(1===k.nodeType)g(k)||"BR"===k.nodeName?(f&&(f.data=f.data.replace(/ $/,"")),f=null,h=!1):k&&b[k.nodeName]&&(f=null,h=!0);else{k=c(k);continue}l=d(r,k);r=k;k=l}f&&(f.data=f.data.replace(/ $/,""),f.data||c(f))}}},{"block-elements":5,"void-elements":6}],5:[function(e,f,h){f.exports="address article aside audio blockquote canvas dd div dl fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 header hgroup hr main nav noscript ol output p pre section table tfoot ul video".split(" ")},
{}],6:[function(e,f,h){f.exports={area:!0,base:!0,br:!0,col:!0,embed:!0,hr:!0,img:!0,input:!0,keygen:!0,link:!0,menuitem:!0,meta:!0,param:!0,source:!0,track:!0,wbr:!0}},{}],7:[function(e,f,h){},{}]},{},[1])(1)});