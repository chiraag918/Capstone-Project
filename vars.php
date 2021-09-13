<?php


function move($dir){
	switch ($dir) {	
		case 'f': forward();	break;
		case 'b': back();	break;
		case 'r': right();	break;
		case 'l': left();	break;
		case 's': stop();	break;	
	}
}

function right(){
    system("gpio -g mode 8 out");
    system("gpio -g write 8 0");
    system("gpio -g mode 7 out");
    system("gpio -g write 7 1");
   
}
function left(){
    system("gpio -g mode 8 out");
    system("gpio -g write 8 1");
    system("gpio -g mode 7 out");
    system("gpio -g write 7 0");
}
function forward(){
    system("gpio -g mode 8 out");
    system("gpio -g write 8 1");
    system("gpio -g mode 7 out");
    system("gpio -g write 7 1");
}
function back(){
	
}
function stop(){
    system("gpio -g mode 8 out");
    system("gpio -g write 8 0");
    system("gpio -g mode 7 out");
    system("gpio -g write 7 0");

}


?>

