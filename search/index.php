---
layout: search
title: "Search"
---

<?php 
$db = new SQLite3('search.db', SQLITE3_OPEN_READONLY);

$query = $_GET['s'];

if ( $query == ""  || preg_match("/^\s+/",$query) ) {
    echo "<h2 class='pagetitle'>No query specified.</h2><div class='entry'>";
}    else {
    echo "<h2 class='pagetitle'>Search Results for '".$query."'</strong></h2><div class='entry'>";

    $query = preg_replace("/^\s+/", "", $query);
    $query = preg_replace("/\s+$/", "", $query);
    $query = preg_replace("/(\s+)(\w+)/", "% %", $query);
    $query = "%" . $query . "%" ;
  
    # Currently returns max of 50 results, count to be used for pagination etc
    $count_stmt = $db->prepare('SELECT count(*) as num_pages FROM pages WHERE title like :search or text_content like :search  or permalink like :search');
    $count_stmt->bindValue(':search', $query, SQLITE3_TEXT);
    $count = $count_stmt->execute();

    $count_result = $count->fetchArray();

    if ( $count_result['num_pages'] == 0){
        #echo "<p>No results for '$query'.</p>";
    } else {
        $results_text = ($count_result['num_pages'] == 1) ? 'result' : 'results';
        $max_results_text = ($count_result['num_pages'] > 50) ? 'Showing first 50 results of ' : '';
        #echo "<p>$max_results_text{$count_result['num_pages']} $results_text for '$query'.</p>";

        $stmt = $db->prepare('SELECT title, permalink, search_excerpt, featured_image, date FROM pages WHERE title like :search or text_content like :search  or permalink like :search or LIMIT 50');
        $stmt->bindValue(':search', $query, SQLITE3_TEXT);

        $result = $stmt->execute();

        /* Show result entry */
        while($search_result = $result->fetchArray(SQLITE3_ASSOC)){
            ?>
	<div class="post type-post status-publish format-standard hentry clearfix">
        <h2 class="title"><a href="<?echo "{$search_result['permalink']}";?>" rel="bookmark" title="Permanent link to '<?echo "{$search_result['title']}";?>'"><?echo "{$search_result['title']}";?></a></h2>
		<div class="postdate">
            <span><?echo date("F jS, Y", strtotime($search_result['date']));?></span> 
            <!--<span>No Comments / 1 comment / 2 comments</span>-->
        </div>

        <div class="entry">
            <?if($search_result['featured_image'] != '') {?>
            <a href="{{ site.baseurl }}{{ post.url }}/"><img width="128" height="128" src="{{ site.baseurl }}/images/<?echo "{$search_result['featured_image']}";?>" class="alignleft post_thumbnail wp-post-image" alt="{{ post.title }}"/></a>
            <?}?>

	        <?echo "{$search_result['search_excerpt']}";?> [...]

            {% comment %}
            {{ post.excerpt }}
            {% endcomment %}
            <div class="readmorecontent">
		        <a class="readmore" href="{{ site.baseurl }}{{ post.url }}/" rel="bookmark" title="Permanent Link to '{{ post.title }}'">Read More &raquo;</a>
	        </div>
        </div>

        <!--TODO
        <div class="postmeta">
            Posted in 
            <a href="http://martin-thoma.com/category/code/" title="View all posts in Code" rel="category tag">Code</a> | 
            Tags: 
            <a href="http://martin-thoma.com/tag/c/" rel="tag">C</a>, <a href="http://martin-thoma.com/tag/puzzle/" rel="tag">puzzle</a> 
        </div> -->
	</div>
<?
        }
    }
}
?>
</div>
