<?
$con = mysql_connect('localhost','root','PASSWORD') # TODO: change your stuff here
    or die('Could not connect to the server!');
 
mysql_select_db('wordpress') 
    or die('Could not select a database.');
 
$sql = 'SELECT  `ID` , guid,  `post_title` ,  `post_content` 
FROM  `wp_posts` 
WHERE  `post_type` =  "attachment"';
$result = mysql_query($sql) 
    or die('A error occured: ' . mysql_error());
;
while($row = mysql_fetch_assoc($result)) {
    $url = explode("http://martin-thoma.com/wp-content/uploads/", $row['guid']);
    $url = "../images/".$url[1];
    echo $row['ID'].";".$url.";\"".$row['post_title']."\";\"".$row['post_content']."\"<br/>";
}

?>
