<?php


function move($dir){
	switch ($dir) {	
		case 'f': forward();	break;
		case 'r': right();	break;
		case 'l': left();	break;
		case 's': stop();	break;	
	}
}

function right(){
    system("echo \"3\"> /dev/ttyS0 38400");
   
}
function left(){
    system("echo \"2\"> /dev/ttyS0 38400");
}
function forward(){
    system("echo \"1\"> /dev/ttyS0 38400");
}
function stop(){
    system("echo \"1\"> /dev/ttyS0 38400");

}


?>

