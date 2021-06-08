/* Validation Setup Start */
function showPopup(message){
    document.getElementById("pop-up").style.display= 'block';
    document.getElementById("pop-up-message").innerText = message;
}
function hidePopup(){
    document.getElementById("pop-up").style.display= 'none';
}
function hideNback(){
    document.getElementById("pop-up").style.display= 'none';
    window.history.back()
}
if(document.getElementById('isServerSite').value == 'True'){
    showPopup(document.getElementById('popup-message').value);
    document.getElementsByTagName('button')[0].removeAttribute('onclick')
    document.getElementsByTagName('button')[0].setAttribute('onclick','hideNback();')
}
/* Setup End */
//code starts affan edited on 19 may 2021 
//remain prpa module validation and on other all edit option of the modules
//task to be resumed  after bug fixing on the prpa module 
//last edited on 26 may 2021
//for the validation of the test 1st question for 2 and 4 marks
function validatetest()
{
  var returnval=true;
  if(document.forms['test']["two_marks1"].value>2 ||  document.forms['test']["two_marks2"].value>2 || document.forms['test']["two_marks3"].value>2 ||document.forms['test']["two_marks4"].value>2 ||document.forms['test']["two_marks5"].value>2 ||document.forms['test']["two_marks6"].value>2 )
  {
      showPopup("the value is invalid exeeding 2");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
     returnval=false;
  }
  if(document.forms['test']["four_marks1"].value>4 ||  document.forms['test']["four_marks2"].value>4 || document.forms['test']["four_marks3"].value>4 ||document.forms['test']["four_marks4"].value>4 ||document.forms['test']["four_marks5"].value>4 )
  {
      showPopup("the value is invalid exceeding 4");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
     returnval=false;
  }
  return returnval;
}
//for the validation of test2 for 2 and 6 marks
function validatetest2()
{
  var returnval1=true;
  if(document.forms['test2']["two_marks1"].value>2 ||  document.forms['test2']["two_marks2"].value>2 || document.forms['test2']["two_marks3"].value>2 ||document.forms['test2']["two_marks4"].value>2 ||document.forms['test2']["two_marks5"].value>2 ||document.forms['test2']["two_marks6"].value>2 )
  {
      showPopup("the value is invalid exeeding 2");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
   returnval1=false;
  }
  else if(document.forms['test2']["six_marks1"].value>6 ||  document.forms['test2']["six_marks2"].value>6 || document.forms['test2']["six_marks3"].value>6 ||document.forms['test2']["six_marks4"].value>6 )
  {
      showPopup("the value is invalid exceeding 6");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
     console.log("the caslu six");
     returnval1=false;
  }
 return returnval1;
}
//for the validation of the index page
function validateIndex()
{
    var year=/^\(?([0-9]{4,4})\)?[-.]?([1-9]{1,2})\)?/g;
    var oly_string=/^[a-zA-Z_ ]+$/g;
    var cosem=/^[A-Z]{2,2}[1-6]{1,1}[A-Z]{1,1}/g;
    var year_inp=document.forms['index']["year"].value;
    var faculty_inp=document.forms['index']["faculty"].value;
    var subject_inp=document.forms['index']["subject"].value;
    var course_Sem_inp=document.forms['index']["courseSemester"].value;
    var returner=true;
    if( year.test(year_inp))
    {
       returner= true;
       console.log("th e invnvea")
    }
    else{
        showPopup("the year should be in YYYY-YY format")
        document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
        //returner= false;
        return false;
    }
    if(oly_string.test(faculty_inp))
    {
        returner= true;
    }
    else{
        showPopup("Please enter valid name")
        document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
        //returner= false;
        return false;
    }
    if(subject_inp.match(oly_string))
    {
        returner=true;
    }
    else{
         showPopup("Please enter valid subject name")
        document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
        //returner= false;
        return false;
    }
    if(course_Sem_inp.match(cosem))
    {
        returner=true;
    }
    else{
         showPopup("Please enter valid Course semester")
        document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
        //returner= false;
        return false;
    }
    
    return returner;
}
//for the validation of the co po mapping
function validateCoMap()
{
  var returnval1=true;
  co_map={
      po1:document.forms['co_map']["po1"].value,
      po2:document.forms['co_map']["po2"].value,
      po3:document.forms['co_map']["po3"].value,
      po4:document.forms['co_map']["po4"].value,
      po5:document.forms['co_map']["po5"].value,
      po6:document.forms['co_map']["po6"].value,
      po7:document.forms['co_map']["po7"].value,
  };
  for (let key in co_map)
  {
      if(co_map.hasOwnProperty(key))
      {
  if(co_map[key]>3 ||co_map[key]<1 )
  {
      showPopup("the value is invalid exeeding 3 or less than 1");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
   returnval1=false;
   return false;
  }
}
}
 return returnval1;
}
function validateCoMap1()
{
  var returnval1=true;
  co_map={
      po11:document.forms['co_map2']["po11"].value,
      po21:document.forms['co_map2']["po21"].value,
      po31:document.forms['co_map2']["po31"].value,
      po41:document.forms['co_map2']["po41"].value,
      po51:document.forms['co_map2']["po51"].value,
      po61:document.forms['co_map2']["po61"].value,
      po71:document.forms['co_map2']["po71"].value,
      pso11:document.forms['co_map2']["pso11"].value,
      pso21:document.forms['co_map2']["pso21"].value,
  };
  for (let key in co_map)
  {
      if(co_map.hasOwnProperty(key))
      {
  if(co_map[key]>3 ||co_map[key]<1 )
  {
      showPopup("the value is invalid exeeding 3 or less than 1");
      document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
   returnval1=false;
   return false;
  }
}
  
}
 return returnval1;
}
function micro_project()
{
  var returnval1=true;
   micro={
       micro1:document.forms['micro_pro1']["micro1"].value,
       micro2:document.forms['micro_pro1']["micro2"].value,
       micro3:document.forms['micro_pro1']["micro3"].value,
       micro4:document.forms['micro_pro1']["micro4"].value,
   }
   for (let key in micro)
   {
       if(micro.hasOwnProperty(key) )
       {
   if(micro[key]>10 )
   {
       showPopup("the value is invalid exeeding 10 or less than 1");
       document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
    returnval1=false;
    return false;
   }
 }
}
 return returnval1;
}
function prpa()
{
  var returnval1=true;
   prpa1={
       prpa1:document.forms['prpa']["prac1"].value+0,
       prpa2:document.forms['prpa']["prac2"].value+0,
       prpa3:document.forms['prpa']["prac3"].value+0,
       prpa4:document.forms['prpa']["prac4"].value+0,
       prpaTotal:document.forms['prpa'].getElementByClassName("total"),
   }
   for (let key in prpa1)
   {
       if(prpa1.hasOwnProperty(key) )
       {
   if(prpa1[key]==0 )
   {
       showPopup("please enter the value in the field");
       document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
    returnval1=false;
    return false;
   }
 }
   }
 if(prpa[4]>50 ||prpa[4]<0)
 {
 showPopup("please enter the value in the prpa field to be less than 51 and greater than or eaqaul to 0");
       document.getElementsByTagName('button')[0].setAttribute('onclick','hidePopup();')
    returnval1=false;
    return false;
 }

 return returnval1;
}