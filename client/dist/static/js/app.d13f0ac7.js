(function(t){function e(e){for(var o,i,s=e[0],l=e[1],c=e[2],p=0,d=[];p<s.length;p++)i=s[p],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&d.push(a[i][0]),a[i]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(t[o]=l[o]);u&&u(e);while(d.length)d.shift()();return r.push.apply(r,c||[]),n()}function n(){for(var t,e=0;e<r.length;e++){for(var n=r[e],o=!0,s=1;s<n.length;s++){var l=n[s];0!==a[l]&&(o=!1)}o&&(r.splice(e--,1),t=i(i.s=n[0]))}return t}var o={},a={app:0},r=[];function i(e){if(o[e])return o[e].exports;var n=o[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.m=t,i.c=o,i.d=function(t,e,n){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var o in t)i.d(n,o,function(e){return t[e]}.bind(null,o));return n},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=e,s=s.slice();for(var c=0;c<s.length;c++)e(s[c]);var u=l;r.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var o=n("2b0e"),a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},r=[],i=n("2877"),s={},l=Object(i["a"])(s,a,r,!1,null,null,null),c=l.exports,u=n("8c4f"),p=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"p-4 h-screen font-sans"},[n("NavBar"),n("div",{staticClass:"px-4 py-20 text-light"},[n("span",{staticClass:"font-bold text-lg"},[t._v("Enter new food")]),n("div",{staticClass:"grid grid-cols-12 gap-4 mt-2"},[n("div",{staticClass:"col-span-9 border-b border-pop"},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],staticClass:"appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full",attrs:{placeholder:"Beef",type:"text"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}})]),n("div",{staticClass:"col-span-2 border-b border-pop"},[n("input",{directives:[{name:"model",rawName:"v-model",value:t.quantity,expression:"quantity"}],staticClass:"appearance-none bg-pop bg-opacity-25 text-pop focus:outline-none w-full",attrs:{placeholder:"100",type:"text"},domProps:{value:t.quantity},on:{input:function(e){e.target.composing||(t.quantity=e.target.value)}}})]),n("div",{staticClass:"col-span-1 font-bold text-lg"},[t._v("g")])]),n("div",{staticClass:"mt-4 mb-2"},[n("span",{staticClass:"font-bold text-lg"},[t._v("Why I ate it")]),n("textarea",{directives:[{name:"model",rawName:"v-model",value:t.reason,expression:"reason"}],staticClass:"h-8 mt-2 p-1 border border-pop rounded appearance-none bg-transparent text-pop text-sm focus:outline-none w-full",attrs:{placeholder:"My mom cooked it"},domProps:{value:t.reason},on:{input:function(e){e.target.composing||(t.reason=e.target.value)}}})]),n("button",{staticClass:"mt-4 rounded bg-light bg-opacity-50 border-light border border-opacity-100 px-2 py-1 text-dark font-bold",on:{click:function(e){return t.createFood()}}},[t._v("Submit")]),n("div",[t._v(t._s(t.confirmation))])])],1)},d=[],f=(n("99af"),n("b0c0"),n("bc3a")),m=n.n(f),v=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},b=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("header",[n("div",{staticClass:"py-2 text-4xl font-bold text-center text-light"},[t._v(" Vegwannabe ")])])}],h={},g=Object(i["a"])(h,v,b,!1,null,null,null),y=g.exports,x={name:"Home",components:{NavBar:y},data:function(){return{name:"",quantity:null,reason:"",confirmation:""}},methods:{createFood:function(){var t=this,e="/foods",n={name:this.name,quantity:this.quantity,date:Date.now(),reason:this.reason};m.a.post(e,n).then((function(e){t.displayValidation(e.data)})),this.name="",this.reason="",this.quantity=0},displayValidation:function(t){this.confirmation="".concat(t.quantity,"g of ").concat(t.name," added on ").concat(t.date)}},created:function(){this.confirmation=""}},_=x,w=Object(i["a"])(_,p,d,!1,null,null,null),O=w.exports,C=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("ul",t._l(t.foods,(function(e){return n("li",{key:e.id},[t._v(" "+t._s(e.name)+" ")])})),0)])},j=[],P={name:"Foods",data:function(){return{foods:{}}},methods:{getFoods:function(){var t=this,e="/foods";m.a.get(e).then((function(e){t.foods=e.data}))}},created:function(){this.getFoods()}},q=P,k=Object(i["a"])(q,C,j,!1,null,null,null),E=k.exports;o["a"].use(u["a"]);var S=new u["a"]({mode:"history",base:"/",routes:[{path:"/",name:"home",component:O},{path:"/display_foods",name:"foods",component:E}]}),$=S;n("a2f0");o["a"].config.productionTip=!1,new o["a"]({router:$,render:function(t){return t(c)}}).$mount("#app")},a2f0:function(t,e,n){}});
//# sourceMappingURL=app.d13f0ac7.js.map