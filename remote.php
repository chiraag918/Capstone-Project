
<html>
<head>        
   <title>Remote</title>  
   <link href="css/remote.css" rel="stylesheet" type="text/css">  
   <script src="js/jquery.min.js"></script>  
   <script src="js/remote.js"></script>  
             
</head> 

<body>
<?php
include_once 'vars.php';



?>
<div align="center" id='box_outer'>
	<!-- =================Direction Buttons=================================================== -->
	<div class='box_row'>
		<input  class="button"  type="submit" onclick="button_direction('f');" value="^^^"/>
	</div>
	<br />
	<div class='box_row'>
		<input class="button" style="float:left" type="submit" onclick="button_direction('l');" value="<<<"/>
		
		<input  class="button" style="float:right" type="submit" onclick="button_direction('r');" value=">>>"/>
	</div>
	<br />
	<div class='box_row'>
			<input class="button" type="submit" onclick="button_direction('s');" value="STOP"/>
	</div>
	<!-- ================================================================================= -->
	
	<br><br>
	

</body>
</html>
