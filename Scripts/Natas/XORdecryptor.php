<?php

$cookie = base64_decode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D');
$data = json_encode(array("showpassword" => "yes", "bgcolor" =>"#ffffff"));

function xor_encrypt($in) {
    $key='KNHL';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print base64_encode(xor_encrypt($data));
?>