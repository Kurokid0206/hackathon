<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>Thank You!</title>
</head>
<body style="text-align: center;padding:20px 0;">
	<?php

		$name = $_POST['contactname'];
		$email = $_POST['contactemail'];
		$number = $_POST['contactnumber'];
		$message = $_POST['contactmessage'];
		
		$formcontent=" From: Cultura Education Form $email \n
		Name: $name \n
		Email Address: $email \n
		Phone Number: $number \n
		Message: $message";
		
		$recipient = "yourdomain@gmail.com";
		$subject = "Cultura Education Contact";
		$mailheader = "From: $email \r\n";
		mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
		
	?>
	
	
</body>
</html>