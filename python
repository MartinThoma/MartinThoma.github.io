<?php
/**
 * This script generates a random password
 *
 * PHP Version 5
 *
 * @category Web_Services
 * @package  Community-chess
 * @author   Martin Thoma <info@martin-thoma.de>
 * @license  http://www.opensource.org/licenses/mit-license.php  MIT License
 * @version  SVN: <svn_id>
 * @link     http://code.google.com/p/community-chess/
 */

function getRandomString($length = 8, $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') {
    $string     = '';
    for ($i = 0; $i < $length; $i++) {
        $string .= $characters[rand(0, strlen($characters)-1)];
    }
    return $string;
}

function addChar($characters, $char) {
    if(strstr($characters, $char) === false) {
        return $characters.$char;
    } else {
        return $characters;
    }
}

function removeChar($characters, $char) {
    if(strstr($characters, $char) === false) {
        return $characters;
    } else {
        $pos = strpos($characters, $char);
        return substr($characters, 0, $pos).substr($characters, $pos+1);
    }
}

if (isset($_POST['submit'])) {
    $characters = "";
    if (isset($_POST['uppercase'])) {
        $setUppercase= true;
        $characters .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    } else {
        $setUppercase= false;
    }

    if (isset($_POST['lowercase'])) {
        $setLowercase= true;
        $characters .= 'abcdefghijklmnopqrstuvwxyz';
    } else {
        $setLowercase= false;
    }

    if (isset($_POST['digits'])) {
        $setDigits   = true;
        $characters .= '0123456789';
    } else {
        $setDigits   = false;
    }

    if (isset($_POST['punctuation'])) {
        $setPunctuation   = true;
        $characters .= '.:,;!?';
    } else {
        $setPunctuation   = false;
    }

    if (isset($_POST['whitespaces'])) {
        $setWhitespaces   = true;
        $characters .= " 	\n";
    } else {
        $setWhitespaces   = false;
    }

    $additions = $_POST['additions'];
    for ($i=0; $i<strlen($additions); $i++) {
        $characters = addChar($characters, substr($additions, $i, 1));
    }

    $removals  = $_POST['removals'];
    for ($i=0; $i<strlen($removals); $i++) {
        $characters = removeChar($characters, substr($removals, $i, 1));
    }

    $length = intval($_POST['length']);
    $genPassword = getRandomString($length, $characters);
} else {
    $setUppercase   = true;
    $setLowercase   = true;
    $setDigits      = true;
    $setPunctuation = false;
    $setWhitespace  = false;
    $additions      = '';
    $removals       = '';
    $length         = 8;
}

?>

<form method="post">
    <fieldset>
        <legend>Allowed Characters</legend>
        <p>
            <label for="uppercase">Upper-case letters (A,B, ..., Z)</label>
            <input type="checkbox" id="uppercase" name="uppercase" <?if($setUppercase){ echo 'checked="checked"';}?> />
        </p>

        <p>
            <label for="lowercase">Lower-case letters (a,b, ..., z)</label>
            <input type="checkbox" id="lowercase" name="lowercase" <?if($setLowercase){ echo 'checked="checked"';}?> />
        </p>

        <p>
            <label for="digits">Digits (0, 1, 2, ... 9)</label>
            <input type="checkbox" id="digits" name="digits" <?if($setDigits){ echo 'checked="checked"';}?> />
        </p>

        <p>
            <label for="punctuation">Punctuation (.:,;!?)</label>
            <input type="checkbox" id="punctuation" name="punctuation" <?if($setPunctuation){ echo 'checked="checked"';}?> />
        </p>

        <p>
            <label for="whitespaces">Whitespace characters (space, tab, newline) WARNING: might be difficult to sent / write down</label>
            <input type="checkbox" id="whitespaces" name="whitespaces" <?if($setWhitespaces){ echo 'checked="checked"';}?>/>
        </p>

        <p>
            <label for="additions">Additions to selection set:</label>
            <input type="text" id="additions" name="additions" value="<?echo $additions;?>"/>
        </p>

        <p>
            <label for="removals">Removals from selection set:</label>
            <input type="text" id="removals" name="removals" value="<?echo $removals;?>"/>
        </p>


    </fieldset>
    <fieldset>
        <p>
            <label for="length">Length of the generated password:</label>
            <input type="text" id="length" name="length" value="<?echo $length;?>"/>
        </p>
    </fieldset>
    <fieldset>
        <input type="submit" id="submit" name="submit"/>
    </fieldset>
</form>

<?php
    if (isset($genPassword)) {
        echo '<p><label for="genPassword">Generated random Password</label>';
        echo '<input type="text" id="genPassword" name="genPassword" value="'.$genPassword.'"/></p>';

        echo "<p>Elements in character set: ".strlen($characters)."</p>";
        echo "<p>Number of characters: ".$length."</p>";
        echo "<p>Possible passwords: ".number_format(pow($length, strlen($characters)))."</p>";
    }
?>
