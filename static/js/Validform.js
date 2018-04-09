
 //及时验证用户名
 function checkuse(){
   //在每个函数中定义check变量是为了在表单提交后，能够逐个验证每个函数是否通过，很好很好。（以下同理）
   var check;
   var username = document.getElementById("username").value;
   if (username.length > 18 || username.length < 6) {
    //此处甚妙，既然你在此处输入错误，那么按理说当然要在此处继续输入了。（在此处继续获取焦点！）
    document.getElementById("username").focus();
    document.getElementById("checktext1").innerHTML='&nbsp;* 用户名输入不合法！';
    check = false;
   } else {
    document.getElementById("checktext1").innerHTML = "&nbsp;√";
    check = true;
   }
   return check;
  };
 //利用正则表达式判断密码符合否
 function checkpwd() {
  var check;
  var reg = /[^A-Za-z0-9_]+/;
  var regs = /^[a-zA-Z0-9_\u4e00-\u9fa5] + $ /;
  var password = document.getElementById("password").value;
  if (password.length < 6 || password.length > 18 || regs.test(password)) {
      document.getElementById("password").focus();
   document.getElementById("checktext2").innerHTML='&nbsp;* 密码输入不合法！';
   check = false;
  } else {
   document.getElementById("checktext2").innerHTML = "&nbsp;√";
   check = true;
  }
  return check;
 };
 //验证密码是否不一致！
 function checkpwdc() {
  var check;
  var password = document.getElementById("password").value;
  var pwdc = document.getElementById("password1").value;
  if (password != pwdc) {
      document.getElementById("password1").focus();
   document.getElementById("checktext3").innerHTML='&nbsp;* 密码不一致！';
   check = false;
  } else {
   document.getElementById("checktext3").innerHTML = "&nbsp;√";
   check = true;
  }
  return check;
 };
  function check() {
  var check = checkuse() && checkpwd() && checkpwdc() && checkemail();
  return check;
 } ;
  //正则表达式验证电子邮件（及时）
 function checkemail(){
  var check;
  //电子邮件的正则表达式
  var e1 = document.getElementById("email").value.indexOf("@",0);
  var e2 = document.getElementById("email").value.indexOf(".",0);
  if(email == "" || (e1==-1 || e2==-1) || e2<e1 )
  {
      document.getElementById("email-error").focus();
   document.getElementById("email-error").innerHTML='&nbsp;* 请输入正确的邮箱！';
   check = false;
  } else {
   document.getElementById("email-error").innerHTML = "&nbsp;√";
   check = true;
  }
  return check;
 } ;