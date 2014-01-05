<?
require_once('wp-load.php');

function getFeaturedImage($postid) {
    $featured_image = "";
    $array = wp_get_attachment_image_src( get_post_thumbnail_id( $post->ID ), 'single-post-thumbnail' );
    if (count($array)>1) {
        $featured_image = $array[0];
        $featured_image = str_replace('http://martin-thoma.com/wp-content/uploads/', '', $featured_image);
    }
    return $featured_image;
}

$args = array(
    'post_type' => 'post',
    'post_status' => 'draft',
    'posts_per_page' => -1 //uncomment this to get all posts
);

$query = new WP_Query($args);
$i=0;
$titles = array();
while ( $query->have_posts() ) : $query->the_post();
    $i++;
    $name = $post->post_name;
    if ($name == "") {
        $name = strtolower(get_the_title());
        $replacements = array(
            ' ' => '-',
            '#' => 'nr',
            '/' => 'or',
            'ö' => 'o',
            'ü' => 'u',
            'ä' => 'a',
            'ß' => 'ss'
        );
        $name = str_replace(array_keys($replacements), $replacements, $name);
    }

    if (array_key_exists($name, $titles)) {
        $name = $post->post_name."-".$post->ID;
    } else {
        $titles[$name] = true;
    }
    echo $name."<br/>";

    $f = fopen("export/".$name. '.md', 'w');
    $content = "---".PHP_EOL;
    $content.= "layout: post".PHP_EOL;
    $content.= "title: ".get_the_title().PHP_EOL;
    $content.= "author: ".get_the_author().PHP_EOL;
    $content.= "date: ".get_the_date('Y-m-d h:i:s').PHP_EOL;
    $content.= "categories: ".PHP_EOL;
    $cats = get_the_category();
    if ($cats) {
        foreach($cats as $category) {
            $content .= '- '.$category->name.PHP_EOL; 
        }
    }
    $content .= 'tags: ';
    $posttags = get_the_tags();

    if ($posttags) {
        $content .= PHP_EOL;
        foreach($posttags as $tag) {
            $content.= "- ".$tag->name.PHP_EOL; 
        }
    } else {
        $content .= "[]".PHP_EOL;
    }
    echo wp_get_attachment_image_src(get_the_post_thumbnail($post->ID));
    $content .= 'featured_image: '.getFeaturedImage($postid).PHP_EOL;
    $content .= '---'.PHP_EOL;    
    $content .= get_the_content();
    fwrite($f, $content);
    fclose($f);
endwhile;
echo $i." posts exported."
?>
