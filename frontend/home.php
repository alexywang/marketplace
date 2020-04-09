<!DOCTYPE html>
<!-- Home Page -->
<html lang = "en">
  <head>
    <meta charset = "utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Home</title>
    <style type = "text/css">
      body {
        font-family: Georgia, serif;
        /*background-color: #d9f2d9;*/
        background-color: #ffece6;
        padding-left: 55px;
        padding-right: 15px;
      }
      #menu {
        padding-top: 15px;
        padding-left: 37px;
      }
      #sitetitle {
        font-size: 35px;
      }
      #logo {
        width: 20px;
        height: 23px;
        padding-right: 10px;
        margin-left: -7px;
      }
      #menupages {
        padding-top: 17px;
        float: right;
        white-space: nowrap;
      }
      .page {
        padding-right: 40px;
        color: black;
      }
      #bulk {
        padding-top: 30px;
      }
      #sidebar {
        float: left;
      }
      li {
        padding-top: 20px;
      }
      .searchbox {
        font-size: 15px;
      }
      #searchicon {
        width: 15px;
        margin-bottom: -2px;
        margin-left: -3px;
        margin-right: -3px;
      }
    </style>
  </head>
  <body>
    <div id="menu">
      <span id="sitetitle"> FurniShare </span>
      <img src="logo.png" alt="Logo" id="logo">
      <span id="menupages">
        <a class="page" href="home.php" style="text-decoration:none">Home</a>
        <a class="page" href="chat.php" style="text-decoration:none">Chat</a>
        <a class="page" href="login.php" style="text-decoration:none">Login</a>
        <a class="page" href="signup.php" style="text-decoration:none">Sign Up</a>
        <a class="page" href="cart.php" style="text-decoration:none">Cart</a>
      </span>
    </div>
    <div id="bulk">
      <div id ="sidebar">
        <ul  style="list-style-type:none;">
          <b>Sort by:</b>
          <p></p>
          <li>Bedroom</li>
          <li>Living Room</li>
          <li>Kitchen</li>
          <li>Seating</li>
          <li>Tables</li>
          <li>Lighting</li>
          <li>Linens</li>
          <li>Decor</li>
          <li>Outdoor</li>
          <li>
            <form action="" id="searchbox">
                <input type="text" placeholder="Search" name="searchinput">
                <button type="submit"><i class="searchbtn"><img src="searchbtn.png" alt="Search" id="searchicon"></i></button>
            </form>
          </li>
        </ul>
      </div>
    </div>
  </body>
</html>
