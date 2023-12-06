<?php
  highlight_file('/var/www/html/index.php');
  include("flag.php");
  $ua = $_SERVER["HTTP_USER_AGENT"];
  $id = md5($_POST["id"]);
  $name = $_GET["name"];
  if ($name == "orgctf")
  {
    echo "就这？<br>";
    if (substr($id,0,5) == "5531a")
    {
      echo "恭喜恭喜！还差一步，请使用ORGCTF_newstar机器获取flag！<br>";
      if ($ua === $allow_ua)
      {
        echo $flag;
      }
    }
  }
?>
