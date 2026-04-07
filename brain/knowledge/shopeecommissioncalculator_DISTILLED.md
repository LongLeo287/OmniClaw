---
id: shopeecommissioncalculator
type: knowledge
owner: OA_Triage
---
# shopeecommissioncalculator
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![Screenshot](https://github.com/arm64x/ShopeeCommissionCalculator/blob/main/screenshot.jpeg)

```

### File: html2canvas.min.js
```js
/*!
 * html2canvas 1.4.1 <https://html2canvas.hertzen.com>
 * Copyright (c) 2022 Niklas von Hertzen <https://hertzen.com>
 * Released under MIT License
 */
!function(A,e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define(e):(A="undefined"!=typeof globalThis?globalThis:A||self).html2canvas=e()}(this,function(){"use strict";
/*! *****************************************************************************
    Copyright (c) Microsoft Corporation.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
    ***************************************************************************** */var r=function(A,e){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(A,e){A.__proto__=e}||function(A,e){for(var t in e)Object.prototype.hasOwnProperty.call(e,t)&&(A[t]=e[t])})(A,e)};function A(A,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function t(){this.constructor=A}r(A,e),A.prototype=null===e?Object.create(e):(t.prototype=e.prototype,new t)}var h=function(){return(h=Object.assign||function(A){for(var e,t=1,r=arguments.length;t<r;t++)for(var B in e=arguments[t])Object.prototype.hasOwnProperty.call(e,B)&&(A[B]=e[B]);return A}).apply(this,arguments)};function a(A,s,o,i){return new(o=o||Promise)(function(t,e){function r(A){try{n(i.next(A))}catch(A){e(A)}}function B(A){try{n(i.throw(A))}catch(A){e(A)}}function n(A){var e;A.done?t(A.value):((e=A.value)instanceof o?e:new o(function(A){A(e)})).then(r,B)}n((i=i.apply(A,s||[])).next())})}function H(t,r){var B,n,s,o={label:0,sent:function(){if(1&s[0])throw s[1];return s[1]},trys:[],ops:[]},A={next:e(0),throw:e(1),return:e(2)};return"function"==typeof Symbol&&(A[Symbol.iterator]=function(){return this}),A;function e(e){return function(A){return function(e){if(B)throw new TypeError("Generator is already executing.");for(;o;)try{if(B=1,n&&(s=2&e[0]?n.return:e[0]?n.throw||((s=n.return)&&s.call(n),0):n.next)&&!(s=s.call(n,e[1])).done)return s;switch(n=0,(e=s?[2&e[0],s.value]:e)[0]){case 0:case 1:s=e;break;case 4:return o.label++,{value:e[1],done:!1};case 5:o.label++,n=e[1],e=[0];continue;case 7:e=o.ops.pop(),o.trys.pop();continue;default:if(!(s=0<(s=o.trys).length&&s[s.length-1])&&(6===e[0]||2===e[0])){o=0;continue}if(3===e[0]&&(!s||e[1]>s[0]&&e[1]<s[3])){o.label=e[1];break}if(6===e[0]&&o.label<s[1]){o.label=s[1],s=e;break}if(s&&o.label<s[2]){o.label=s[2],o.ops.push(e);break}s[2]&&o.ops.pop(),o.trys.pop();continue}e=r.call(t,o)}catch(A){e=[6,A],n=0}finally{B=s=0}if(5&e[0])throw e[1];return{value:e[0]?e[1]:void 0,done:!0}}([e,A])}}}function t(A,e,t){if(t||2===arguments.length)for(var r,B=0,n=e.length;B<n;B++)!r&&B in e||((r=r||Array.prototype.slice.call(e,0,B))[B]=e[B]);return A.concat(r||e)}var d=(B.prototype.add=function(A,e,t,r){return new B(this.left+A,this.top+e,this.width+t,this.height+r)},B.fromClientRect=function(A,e){return new B(e.left+A.windowBounds.left,e.top+A.windowBounds.top,e.width,e.height)},B.fromDOMRectList=function(A,e){e=Array.from(e).find(function(A){return 0!==A.width});return e?new B(e.left+A.windowBounds.left,e.top+A.windowBounds.top,e.width,e.height):B.EMPTY},B.EMPTY=new B(0,0,0,0),B);function B(A,e,t,r){this.left=A,this.top=e,this.width=t,this.height=r}for(var f=function(A,e){return d.fromClientRect(A,e.getBoundingClientRect())},Q=function(A){for(var e=[],t=0,r=A.length;t<r;){var B,n=A.charCodeAt(t++);55296<=n&&n<=56319&&t<r?56320==(64512&(B=A.charCodeAt(t++)))?e.push(((1023&n)<<10)+(1023&B)+65536):(e.push(n),t--):e.push(n)}return e},g=function(){for(var A=[],e=0;e<arguments.length;e++)A[e]=arguments[e];if(String.fromCodePoint)return String.fromCodePoint.apply(String,A);var t=A.length;if(!t)return"";for(var r=[],B=-1,n="";++B<t;){var s=A[B];s<=65535?r.push(s):(s-=65536,r.push(55296+(s>>10),s%1024+56320)),(B+1===t||16384<r.length)&&(n+=String.fromCharCode.apply(String,r),r.length=0)}return n},e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",n="undefined"==typeof Uint8Array?[]:new Uint8Array(256),s=0;s<e.length;s++)n[e.charCodeAt(s)]=s;for(var o="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",c="undefined"==typeof Uint8Array?[]:new Uint8Array(256),i=0;i<o.length;i++)c[o.charCodeAt(i)]=i;function w(A,e,t){return A.slice?A.slice(e,t):new Uint16Array(Array.prototype.slice.call(A,e,t))}var U=(l.prototype.get=function(A){var e;if(0<=A){if(A<55296||56319<A&&A<=65535)return e=this.index[A>>5],this.data[e=(e<<2)+(31&A)];if(A<=65535)return e=this.index[2048+(A-55296>>5)],this.data[e=(e<<2)+(31&A)];if(A<this.highStart)return e=this.index[e=2080+(A>>11)],e=this.index[e+=A>>5&63],this.data[e=(e<<2)+(31&A)];if(A<=1114111)return this.data[this.highValueIndex]}return this.errorValue},l);function l(A,e,t,r,B,n){this.initialValue=A,this.errorValue=e,this.highStart=t,this.highValueIndex=r,this.index=B,this.data=n}for(var C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",u="undefined"==typeof Uint8Array?[]:new Uint8Array(256),F=0;F<C.length;F++)u[C.charCodeAt(F)]=F;function p(A,e,t,r){var B=r[t];if(Array.isArray(A)?-1!==A.indexOf(B):A===B)for(var n=t;n<=r.length;){if((o=r[++n])===e)return 1;if(o!==D)break}if(B===D)for(n=t;0<n;){var s=r[--n];if(Array.isArray(A)?-1!==A.indexOf(s):A===s)for(var o,i=t;i<=r.length;){if((o=r[++i])===e)return 1;if(o!==D)break}if(s!==D)break}}function E(A,e){for(var t=A;0<=t;){var r=e[t];if(r!==D)return r;t--}return 0}function I(t,A){var e=(B=function(A,r){void 0===r&&(r="strict");var B=[],n=[],s=[];return A.forEach(function(A,e){var t=rA.get(A);if(50<t?(s.push(!0),t-=50):s.push(!1),-1!==["normal","auto","loose"].indexOf(r)&&-1!==[8208,8211,12316,12448].indexOf(A))return n.push(e),B.push(16);if(4!==t&&11!==t)return n.push(e),31===t?B.push("strict"===r?O:q):t===AA||29===t?B.push(J):43===t?131072<=A&&A<=196605||196608<=A&&A<=262141?B.push(q):B.push(J):void B.push(t);if(0===e)return n.push(e),B.push(J);t=B[e-1];return-1===iA.indexOf(t)?(n.push(n[e-1]),B.push(t)):(n.push(e),B.push(J))}),[n,B,s]}(t,(A=A||{lineBreak:"normal",wordBreak:"normal"}).lineBreak))[0],r=B[1],B=B[2];return[e,r="break-all"===A.wordBreak||"break-word"===A.wordBreak?r.map(function(A){return-1!==[R,J,AA].indexOf(A)?q:A}):r,"keep-all"===A.wordBreak?B.map(function(A,e){return A&&19968<=t[e]&&t[e]<=40959}):void 0]}var y,K,m,L,b,D=10,v=13,x=15,M=17,S=18,T=19,G=20,O=21,V=22,k=24,R=25,N=26,P=27,X=28,J=30,Y=32,W=33,Z=34,_=35,q=37,j=38,z=39,$=40,AA=42,eA=[9001,65288],tA="×",rA=(m=function(A){var e,t,r,B,n=.75*A.length,s=A.length,o=0;"="===A[A.length-1]&&(n--,"="===A[A.length-2]&&n--);for(var n=new("undefined"!=typeof ArrayBuffer&&"undefined"!=typeof Uint8Array&&void 0!==Uint8Array.prototype.slice?ArrayBuffer:Array)(n),i=Array.isArray(n)?n:new Uint8Array(n),Q=0;Q<s;Q+=4)e=c[A.charCodeAt(Q)],t=c[A.charCodeAt(Q+1)],r=c[A.charCodeAt(Q+2)],B=c[A.charCodeAt(Q+3)],i[o++]=e<<2|t>>4,i[o++]=(15&t)<<4|r>>2,i[o++]=(3&r)<<6|63&B;return n}(y="KwAAAAAAAAAACA4AUD0AADAgAAACAAAAAAAIABAAGABAAEgAUABYAGAAaABgAGgAYgBqAF8AZwBgAGgAcQB5AHUAfQCFAI0AlQCdAKIAqgCyALoAYABoAGAAaABgAGgAwgDKAGAAaADGAM4A0wDbAOEA6QDxAPkAAQEJAQ8BFwF1AH0AHAEkASwBNAE6AUIBQQFJAVEBWQFhAWgBcAF4ATAAgAGGAY4BlQGXAZ8BpwGvAbUBvQHFAc0B0wHbAeMB6wHxAfkBAQIJAvEBEQIZAiECKQIxAjgCQAJGAk4CVgJeAmQCbAJ0AnwCgQKJApECmQKgAqgCsAK4ArwCxAIwAMwC0wLbAjAA4wLrAvMC+AIAAwcDDwMwABcDHQMlAy0DNQN1AD0DQQNJA0kDSQNRA1EDVwNZA1kDdQB1AGEDdQBpA20DdQN1AHsDdQCBA4kDkQN1AHUAmQOhA3UAdQB1AHUAdQB1AHUAdQB1AHUAdQB1AHUAdQB1AHUAdQB1AKYDrgN1AHUAtgO+A8YDzgPWAxcD3gPjA+sD8wN1AHUA+wMDBAkEdQANBBUEHQQlBCoEFwMyBDgEYABABBcDSARQBFgEYARoBDAAcAQzAXgEgASIBJAEdQCXBHUAnwSnBK4EtgS6BMIEyAR1AHUAdQB1AHUAdQCVANAEYABgAGAAYABgAGAAYABgANgEYADcBOQEYADsBPQE/AQEBQwFFAUcBSQFLAU0BWQEPAVEBUsFUwVbBWAAYgVgAGoFcgV6BYIFigWRBWAAmQWfBaYFYABgAGAAYABgAKoFYACxBbAFuQW6BcEFwQXHBcEFwQXPBdMF2wXjBeoF8gX6BQIGCgYSBhoGIgYqBjIGOgZgAD4GRgZMBmAAUwZaBmAAYABgAGAAYABgAGAAYABgAGAAYABgAGIGYABpBnAGYABgAGAAYABgAGAAYABgAGAAYAB4Bn8GhQZgAGAAYAB1AHcDFQSLBmAAYABgAJMGdQA9A3UAmwajBqsGqwaVALMGuwbDBjAAywbSBtIG1QbSBtIG0gbSBtIG0gbdBuMG6wbzBvsGAwcLBxMHAwcbByMHJwcsBywHMQcsB9IGOAdAB0gHTgfSBkgHVgfSBtIG0gbSBtIG0gbSBtIG0gbSBiwHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAdgAGAALAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAdbB2MHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsBywHLAcsB2kH0gZwB64EdQB1AHUAdQB1AHUAdQB1AHUHfQdgAIUHjQd1AHUAlQedB2AAYAClB6sHYACzB7YHvgfGB3UAzgfWBzMB3gfmB1EB7gf1B/0HlQENAQUIDQh1ABUIHQglCBcDLQg1CD0IRQhNCEEDUwh1AHUAdQBbCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIaQhjCGQIZQhmCGcIaAhpCGMIZAhlCGYIZwhoCGkIYwhkCGUIZghnCGgIcAh3CHoIMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwAIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIgggwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAAMAAwADAALAcsBywHLAcsBywHLAcsBywHLAcsB4oILAcsB44I0gaWCJ4Ipgh1AHUAqgiyCHUAdQB1AHUAdQB1AHUAdQB1AHUAtwh8AXUAvwh1AMUIyQjRCNkI4AjoCHUAdQB1AO4I9gj+CAYJDgkTCS0HGwkjCYIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiCCIIIggiAAIAAAAFAAYABgAGIAXwBgAHEAdQBFAJUAogCyAKAAYABgAEIA4ABGANMA4QDxAMEBDwE1AFwBLAE6AQEBUQF4QkhCmEKoQrhCgAHIQsAB0MLAAcABwAHAAeDC6ABoAHDCwMMAAcABwAHAAdDDGMMAAcAB6MM4wwjDWMNow3jDaABoAGgAaABoAGgAaABoAGgAaABoAGgAaABoAGgAaABoAGgAaABoAEjDqABWw6bDqABpg6gAaABoAHcDvwOPA+gAaABfA/8DvwO/A78DvwO/A78DvwO/A78DvwO/A78DvwO/A78DvwO/A78DvwO/A78DvwO/A78DvwO/A78DpcPAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcABwAHAAcAB9cPKwkyCToJMAB1AHUAdQBCCUoJTQl1AFUJXAljCWcJawkwADAAMAAwAHMJdQB2CX4JdQCECYoJjgmWCXUAngkwAGAAYABxAHUApgn3A64JtAl1ALkJdQDACTAAMAAwADAAdQB1AHUAdQB1AHUAdQB1AHUAowYNBMUIMAAwADAAMADICcsJ0wnZCRUE4QkwAOkJ8An4CTAAMAB1AAAKvwh1AAgKDwoXCh8KdQAwACcKLgp1ADYKqAmICT4KRgowADAAdQB1AE4KMAB1AFYKdQBeCnUAZQowADAAMAAwADAAMAAwADAAMAAVBHUAbQowADAAdQC5CXUKMAAwAHwBxAijBogEMgF9CoQKiASMCpQKmgqIBKIKqgquCogEDQG2Cr4KxgrLCjAAMADTCtsKCgHjCusK8Qr5CgELMAAwADAAMAB1AIsECQsRC3UANAEZCzAAMAAwADAAMAB1ACELKQswAHUANAExCzkLdQBBC0kLMABRC1kLMAAwADAAMAAwADAAdQBhCzAAMAAwAGAAYABpC3ELdwt/CzAAMACHC4sLkwubC58Lpwt1AK4Ltgt1APsDMAAwADAAMAAwADAAMAAwAL4LwwvLC9IL1wvdCzAAMADlC+kL8Qv5C/8LSQswADAAMAAwADAA
... [TRUNCATED]
```

### File: manifest.json
```json
{
    "manifest_version": 3,
    "name": "Commission Calculator",
    "version": "1.2",
    "description": "Tính hoa hồng và số đơn hàng Shopee khi đã có chuyển đổi.",
    "action": {
        "default_popup": "popup.html",
        "default_icon": {
            "16": "icon16.png",
            "32": "icon32.png",
            "48": "icon48.png",
            "128": "icon128.png"
        }
    },
    "permissions": [
        "activeTab",
        "scripting"
    ],
    "icons": {
        "16": "icon16.png",
        "32": "icon32.png",
        "48": "icon48.png", 
        "128": "icon128.png"
    }
}

```

### File: popup.html
```html
<!DOCTYPE html>
<html lang="vi" data-bs-theme="dark" id="mainContainer">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Commission Calculator</title>
    <link rel="stylesheet" href="styles.css">
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="html2canvas.min.js"></script>
    <style>
        .commission-box {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 5px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .xtra-commission { background-color: #007bff; color: white; }
        .total-commission { background-color: #28a745; color: white; }
        .shopee-commission { background-color: #17a2b8; color: white; }
        /* Style cho nút chụp ảnh */
    #captureBtn {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 1000;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: rgba(13, 110, 253, 0.9);
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    #captureBtn:hover {
        background-color: rgba(13, 110, 253, 1);
        transform: scale(1.05);
    }
    
    #captureBtn svg {
        width: 20px;
        height: 20px;
    }

    /* Toast notification style */
    .toast-notification {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: rgba(25, 135, 84, 0.9);
        color: white;
        padding: 10px 20px;
        border-radius: 4px;
        z-index: 1000;
        animation: fadeInOut 2s ease-in-out forwards;
    }

    @keyframes fadeInOut {
        0% { opacity: 0; transform: translateY(20px); }
        20% { opacity: 1; transform: translateY(0); }
        80% { opacity: 1; transform: translateY(0); }
        100% { opacity: 0; transform: translateY(-20px); }
    }
    </style>
</head>
<body>
    <div class="container mt-4">
        <!-- Cập nhật nút chụp ảnh trong body -->
        <button id="captureBtn" class="btn btn-primary" title="Chụp ảnh">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z"/>
                <path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0"/>
            </svg>
        </button>
        <h1 class="text-center mb-4">Công cụ tính Shopee - Lê Tí</h1>
        <div id="result">
        <div class="row mb-3">
            <div class="col-4">
                <div class="commission-box total-commission">
                    <span>Tổng hoa hồng</span>
                    <p class="fs-4 mb-0" id="totalCommission">Đang xử lý...</p>
                </div>
            </div>
            <div class="col-4">
                <div class="commission-box xtra-commission">
                    <span>Xtra</span>
                    <p class="fs-4 mb-0" id="xtraCommission">Đang xử lý...</p>
                </div>
            </div>
            <div class="col-4">
                <div class="commission-box shopee-commission">
                    <span>Shopee</span>
                    <p class="fs-4 mb-0" id="shopeeCommission">Đang xử lý...</p>
                </div>
            </div>
        </div>

        <p class="text-center">Ngày: <span id="startDate"></span><span id="endDate"></span></p>

        <div id="dateWarning" class="alert alert-warning text-center" style="display: none;">
            Bạn đang xem kết quả của nhiều ngày khác nhau.
        </div>

        <div class="row">
                    <div class="col-12">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Loại đơn hàng</th>
                                    <th>Số đơn</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Tổng</td>
                                    <td id="totalOrders">Đang xử lý...</td>
                                </tr>
                                
                                <tr>
                                    <td>Đơn video</td>
                                    <td id="videoOrders">Đang xử lý...</td>
                                </tr>
                                <tr>
                                    <td>Đơn live</td>
                                    <td id="liveOrders">Đang xử lý...</td>
                                </tr>
                                <tr>
                                    <td>Đơn social</td>
                                    <td id="socialOrders">Đang xử lý...</td>
                                </tr>
                                <tr>
                                    <td>Đơn 0đ</td>
                                    <td id="zeroCommissionOrders">Đang xử lý...</td>
                                </tr>
                                <tr>
                                    <td>Đơn chưa thanh toán</td>
                                    <td id="unpaidOrders">Đang xử lý...</td>
                                </tr>
                                <tr>
                                    <td>Đơn hủy</td>
                                    <td id="canceledOrders">Đang xử lý...</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
        </div>

        <div class="row mt-3">
            <div class="col-12 text-center">
                <div id="paginationWarning" class="alert alert-danger" style="display: none;">
                    Có nhiều hơn 1 trang hiển thị, hãy kéo xuống dưới cùng và chọn trang 1.
                </div>
                <button id="scrollToBottom" class="btn btn-secondary" style="display: none;">Cuộn xuống cuối trang</button>
            </div>
        </div>
        </div>

    
    </div>

    <script src="popup.js"></script>
</body>
</html>
```

### File: popup.js
```js
document.addEventListener('DOMContentLoaded', function () {

    // Kiểm tra URL hiện tại
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const currentUrl = tabs[0].url;
        const urlPattern = /\/report\/conversion_report/; // Biểu thức chính quy để kiểm tra phần đường dẫn

        if (!urlPattern.test(currentUrl)) {
            const urlObj = new URL(currentUrl); // Lấy domain từ URL hiện tại
            const expectedUrl = `${urlObj.origin}/report/conversion_report`; // Tạo đường dẫn đầy đủ

            document.getElementById('result').style.display = 'none'; // Ẩn kết quả nếu URL không đúng
            document.getElementById('paginationWarning').style.display = 'none'; // Ẩn cảnh báo phân trang nếu URL không đúng
            document.getElementById('scrollToBottom').style.display = 'none'; // Ẩn nút cuộn nếu URL không đúng

            const usageInstructions = `
                <p>1. Truy cập <a href="${expectedUrl}" target="_blank">${expectedUrl}</a><br>
                2. Bấm vào biểu tượng hình răng cưa và tick vào ô Thông tin bổ sung<br>
                3. Chọn ngày cần xem kết quả<br>4. Bấm vào Tìm kiếm để lọc dữ liệu<br>5. Nếu quá nhiều đơn hàng hãy kéo xuống dưới cùng bấm vào chọn 100/trang<br>6. Bấm vào biểu tượng extension để xem kết quả.</p>
            `;
            document.body.innerHTML += usageInstructions; // Thêm hướng dẫn sử dụng vào cuối nội dung
        } else {
            // Nếu URL đúng, tính tổng hoa hồng và hiển thị kết quả
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: calculateAllPages
            }, (results) => {
                if (results && results[0]) {
                    const { totalCommission, xtraCommission, shopeeCommission, totalOrders, canceledOrders, unpaidOrders, videoOrders, liveOrders, socialOrders, zeroCommissionOrders, startDate, endDate, dateWarning } = results[0].result;

                    // Hàm format lại ngày
                    function formatDate(dateString) {
                        if (!dateString) return '';
                        
                        // Tách chuỗi theo dấu gạch ngang
                        const parts = dateString.split('-');
                        
                        // Đảm bảo có đủ 3 phần
                        if (parts.length === 3) {
                            const [day, month, year] = parts;
                            return `${day}/${month}/${year}`;
                        }
                        
                        return dateString;
                    }
                                        
                    const startDateFormatted = formatDate(startDate);
                    const endDateFormatted = formatDate(endDate);

                    if (startDate === endDate) {
                        document.getElementById('startDate').textContent = startDateFormatted;
                        document.getElementById('endDate').textContent = '';
                    } else {
                        document.getElementById('startDate').textContent = startDateFormatted;
                        document.getElementById('endDate').textContent = ` - ${endDateFormatted}`;
                    }

                    // Hiển thị cảnh báo nếu các ngày khác nhau
                    if (dateWarning) {
                        document.getElementById('dateWarning').style.display = 'block';
                    } else {
                        document.getElementById('dateWarning').style.display = 'none';
                    }

                    document.getElementById('totalCommission').textContent = totalCommission;
                    document.getElementById('xtraCommission').textContent = xtraCommission;
                    document.getElementById('shopeeCommission').textContent = shopeeCommission;
                    //document.getElementById('totalOrders').textContent = totalOrders;
                    document.getElementById('totalOrders').innerHTML = totalOrders;
                    document.getElementById('canceledOrders').textContent = canceledOrders;
                    document.getElementById('unpaidOrders').textContent = unpaidOrders;
                    document.getElementById('videoOrders').textContent = videoOrders;
                    document.getElementById('liveOrders').textContent = liveOrders;
                    document.getElementById('zeroCommissionOrders').textContent = zeroCommissionOrders;

                    // Kiểm tra nếu unpaidOrders lớn hơn 0 thì hiển thị dòng này
                    if (unpaidOrders > 0) {
                        const unpaidElement = document.getElementById('unpaidOrders');
                        unpaidElement.parentElement.classList.remove('d-none');
                        unpaidElement.innerHTML = `<span class="badge bg-secondary">${unpaidOrders}</span>`;
                    } else {
                        document.getElementById('unpaidOrders').parentElement.classList.add('d-none');
                    }

                    // Kiểm tra nếu liveOrders lớn hơn 0 thì hiển thị dòng này
                    if (liveOrders > 0) {
                        document.getElementById('liveOrders').parentElement.classList.remove('d-none');
                        document.getElementById('liveOrders').textContent = liveOrders;
                    } else {
                        document.getElementById('liveOrders').parentElement.classList.add('d-none');
                    }

                    // Kiểm tra nếu videoOrders lớn hơn 0 thì hiển thị dòng này
                    if (videoOrders > 0) {
                        document.getElementById('videoOrders').parentElement.classList.remove('d-none');
                        document.getElementById('videoOrders').textContent = videoOrders;
                    } else {
                        document.getElementById('videoOrders').parentElement.classList.add('d-none');
                    }

                    // Kiểm tra nếu canceledOrders lớn hơn 0 thì hiển thị dòng này
                    if (canceledOrders > 0) {
                        const canceledElement = document.getElementById('canceledOrders');
                        canceledElement.parentElement.classList.remove('d-none');
                        canceledElement.innerHTML = `<span class="badge bg-danger">${canceledOrders}</span>`;
                    } else {
                        document.getElementById('canceledOrders').parentElement.classList.add('d-none');
                    }

                    // Kiểm tra nếu socialOrders lớn hơn 0 thì hiển thị dòng này
                    if (socialOrders > 0) {
                        document.getElementById('socialOrders').parentElement.classList.remove('d-none');
                        document.getElementById('socialOrders').textContent = socialOrders;
                    } else {
                        document.getElementById('socialOrders').parentElement.classList.add('d-none');
                    }

                    // Kiểm tra nếu zeroCommissionOrders lớn hơn 0 thì hiển thị dòng này
                    if (zeroCommissionOrders > 0) {
                        document.getElementById('zeroCommissionOrders').parentElement.classList.remove('d-none');
                        document.getElementById('zeroCommissionOrders').innerHTML = `<span class="badge bg-warning text-dark">${zeroCommissionOrders}</span>`;
                    } else {
                        document.getElementById('zeroCommissionOrders').parentElement.classList.add('d-none');
                    }

                }
            });

            // Thêm sự kiện cho nút cuộn xuống cuối trang
            document.getElementById('scrollToBottom').addEventListener('click', function() {
                chrome.scripting.executeScript({
                    target: { tabId: tabs[0].id },
                    function: scrollToBottom
                });
            });
        }
    });

    // Thêm xử lý sự kiện cho nút chụp ảnh
    document.getElementById('captureBtn')?.addEventListener('click', async function() {
        try {
            // Ẩn nút chụp trước khi chụp
            const captureBtn = document.getElementById('captureBtn');
            captureBtn.style.visibility = 'hidden';
            
            // Chụp toàn bộ container
            const canvas = await html2canvas(document.documentElement, {
                backgroundColor: '#ffffff',
                scale: 2,
                logging: false,
                useCORS: true
            });
            
            // Chuyển canvas thành blob
            canvas.toBlob(async function(blob) {
                try {
                    // Copy ảnh vào clipboard
                    const clipboardItem = new ClipboardItem({ 'image/png': blob });
                    await navigator.clipboard.write([clipboardItem]);
                    
                    // Hiện thông báo thành công
                    const toast = document.createElement('div');
                    toast.className = 'toast-notification';
                    toast.textContent = 'Đã copy ảnh vào bộ nhớ đệm!';
                    document.body.appendChild(toast);
                    
                    // Xóa toast sau khi animation kết thúc
                    setTimeout(() => {
                        document.body.removeChild(toast);
                    }, 2000);
                } catch (error) {
                    console.error('Error copying to clipboard:', error);
                    alert('Không thể copy ảnh vào bộ nhớ đệm. Vui lòng thử lại.');
                }
                
                // Hiện lại nút chụp
                captureBtn.style.visibility = 'visible';
            }, 'image/png');
            
        } catch (error) {
            console.error('Error capturing screenshot:', error);
            alert('Có lỗi khi chụp ảnh. Vui lòng thử lại.');
            document.getElementById('captureBtn').style.visibility = 'visible';
        }
    });
});


// Hàm cuộn xuống cuối trang
function scrollToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
}

// Hàm tính tổng hoa hồng và xử lý nhiều trang
async function calculateAllPages() {
    let totalCommission = 0;
    let xtraCommission = 0;
    let shopeeCommission = 0;
    let totalOrders = 0;
    let canceledOrders = 0;
    let unpaidOrders = 0;
    let videoOrders = 0;
    let liveOrders = 0;
    let socialOrders = 0;
    let zeroCommissionOrders = 0; // Thêm biến đếm đơn 0đ

    // Kiểm tra ngày bắt đầu và kết thúc
    const startDateInput = document.querySelector('.ant-calendar-range-picker-input:nth-child(1)');
    const endDateInput = document.querySelector('.ant-calendar-range-picker-input:nth-child(3)');

    // Lấy giá trị trực tiếp từ value của input
    const startDate = startDateInput ? startDateInput.value : '';
    const endDate = endDateInput ? endDateInput.value : '';
    
    let dateWarning = startDate !== endDate;

    // Hàm tính toán hoa hồng cho một trang
    function calculateCurrentPage() {
        const commissionElements = document.querySelectorAll('li.commission-top-bold span');

        commissionElements.forEach(element => {
            const commissionText = element.textContent.trim();
            const commission = parseFloat(commissionText.replace(/[₫,.]/g, '').replace(/,/g, '.'));

            if (!isNaN(commission)) {
                totalCommission += commission;
                
                // Đếm số đơn có hoa hồng 0đ
                if (commission === 0) {
                    zeroCommissionOrders++;
                }
            }
        });

        // Tính hoa hồng Xtra
        const xtraCommissionElements = document.querySelectorAll('.commission-wrap ul li');
        xtraCommissionElements.forEach(element => {
            const xtraText = element.textContent;
            if (xtraText.includes('Hoa hồng Xtra')) {
                const commissionText = xtraText.split(':')[1].trim();
                const commission = parseFloat(commissionText.replace(/[₫,.]/g, '').replace(/,/g, '.'));

                if (!isNaN(commission)) {
                    xtraCommission += commission;
                }
            }
        });

        // Tính hoa hồng Shopee
        const shopeeCommissionElements = document.querySelectorAll('.commission-wrap ul li');
        shopeeCommissionElements.forEach(element => {
            const shopeeText = element.textContent;
            if (shopeeText.includes('Hoa hồng từ Shopee')) {
                const commissionText = shopeeText.split(':')[1].trim();
                const commission = parseFloat(commissionText.replace(/[₫,.]/g, '').replace(/,/g, '.'));

                if (!isNaN(commission)) {
                    shopeeCommission += commission;
                }
            }
        });

        const orderElements = document.querySelectorAll('span.report-table-label.report-table-label-medium');
        totalOrders += orderElements.length / 4;

        const canceledElements = document.querySelectorAll('span.an-tag[style*="color: rgb(153, 153, 153);"]');
        canceledElements.forEach(element => {
            const statusText = element.textContent.trim();
            if (statusText === 'Đã hủy') {
                canceledOrders++;
            } else if (statusText === 'Chưa thanh toán') {
                unpaidOrders++;
            }
        });

        //canceledOrders /= 2;
        //unpaidOrders /= 2;

        const videoElements = document.querySelectorAll('span.report-table-value-text.report-table-value-text-large');
        videoElements.forEach(element => {
            const statusText = element.textContent.trim();
            if (statusText === 'Shopeevideo-Shopee') {
                videoOrders++;
            } else if (statusText === 'Shopeelive-Shopee') {
                liveOrders++;
            }
        });
    }


    // Hàm để chuyển qua trang kế và xử lý
    async function processNextPage() {
        const nextPageButton = document.querySelector('.ant-pagination-next');

        if (nextPageButton && !nextPageButton.classList.contains('ant-pagination-disabled')) {
            nextPageButton.click();
            await new Promise(resolve => setTimeout(resolve, 3000)); // Đợi trang tải xong
            calculateCurrentPage(); // Tính toán dữ liệu của trang hiện tại
            return processNextPage(); // Gọi lại để xử lý các trang kế
        } else {
            console.log('Đã đến trang cuối cùng.');
            return {
                totalCommission: totalCommission.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' }),
                xtraCommission: (xtraCommission / 2).toLocaleString('vi-VN', { style: 'currency', currency: 'VND' }),
                shopeeCommission: (shopeeCommission / 2).toLocaleString('vi-VN', { style: 'currency', currency: 'VND' }),
                totalOrders: `${totalOrders - canceledOrders / 2 - un
... [TRUNCATED]
```

### File: styles.css
```css
html {
    width: 500px;
}

body {
    font-family: Arial, sans-serif;
    padding: 10px;
    max-width: 500px;
}

h1 {
    font-size: 18px;
    margin-bottom: 15px;
}

p {
    margin: 10px 0;
    font-size: 14px;
}

#result span {
    font-weight: bold;
}

```

