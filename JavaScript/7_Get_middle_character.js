function getMiddle(s)
{
  var len = s.length;
  if (len % 2 != 0){
    return s.charAt(len/2);
  }
  else{
    return s.charAt((len-1)/2) + s.charAt(len/2)
  }
}