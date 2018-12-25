---
layout: post
title: WhatsApp Data
slug: whatsapp-data
author: Martin Thoma
date: 2018-12-23 20:00
category: My bits and bytes
tags: Machine Learning, WhatsApp, Text Mining, Pandas
featured_image: logos/ml.png
---
As a data scientist, I'm always interested in exporting and analyzing data. One
especially when it is my own data. WhatsApp is one big personal data source
which I couldn't analyze so far.


## Other Analysis

I've seen WhatsApp data analysis on [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/)
a couple of times:

<table>
    <tr>
        <th></th>
        <th>Data Set</th>
        <th>Analysis Techniques</th>
        <th>Tools</th>
    </tr>
    <tr>
        <td>14.3k</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/8fl589/i_built_a_tool_to_visualize_whatsapp_chats_here/">Here is the result of the chat history with my girlfriend!</a></td>
        <td></td>
        <td>R, <a href="https://chatanalyzer.moritzwolf.com/">Website</a></td>
    </tr>
    <tr>
        <td>6484</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/5pi9sn/my_year_in_facebook_messages_created_with_d3js_oc/">My Year in Facebook Messages</a></td>
        <td>*&nbsp;Radar chart</td>
        <td>D3js</td>
    </tr>
    <tr>
        <td>982</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/8bh5tx/a_word_cloud_i_generated_from_the_texts_between/">A word Cloud I generated from the texts between my girlfriend and me</a></td>
        <td>* Word cloud</td>
        <td></td>
    </tr>
    <tr>
        <td>946</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/64s3hg/ploting_my_2_years_old_whatsapp_chat_with_my_gf_oc/">Ploting my 2 years old WhatsApp chat with my GF</a></td>
        <td>* Bar chart (Group by=Weekday, height=Number of images received)<br/>* Density plot (x=Hour of the day, height=Number of messages)</td>
        <td></td>
    </tr>
    <tr>
        <td>205</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/8ogo4w/after_3_years_of_relationship_i_decided_to_do_a/">After 3 Years of Relationship I decided to do a WhatsApp Analysis</a></td>
        <td>* Radar chart<br/>*&nbsp;</td>
        <td>???</td>
    </tr>
    <tr>
        <td></td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/a8nwkg/oc_facebook_and_whatsapp_message_history_of_a/">Facebook and WhatsApp message history of a four-year long-distance relationship</a></td>
        <td>* Line chart (x=Days, y=Number of messages on that day)</td>
        <td>*&nbsp;Facebook data dump and WhatsApp message backups*&nbsp;Python (matplotlib and imageio)</td>
    </tr>
    <tr>
        <td></td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/a8gwn0/oc_texts_received_from_classmates_per_day_leading/">Texts received from classmates per day leading up to exams</a></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>153</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/a6ieu6/oc_whatsapp_visualizer_i_made_a_webpage_to/">WhatsApp Visualizer</a></td>
        <td>* Bar chart (Group by=Person, Height=Number of Messages exchanged)<br/>* Bar chart (Group by=Person, Height=Number of words exchanged)<br/>* Bar chart (Group by=word, Height=Count of word in the dataset)<br/>* Pie chart (Sections=Person, Amount=Media sent by that person)<br/>* Line chart (x=Hour of the day, y=Messages sent)</td>
        <td><a href="https://ameyrk.me/whatsapp-visualizer/">Website</a></td>
    </tr>
    <tr>
        <td>4</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/88le7m/whatsapp_images_recieved_each_day_of_the_weekoc/">Whatsapp Images Recieved Each Day of the Week</a></td>
        <td>* Bar chart (Group by=Weekday, height=Number of images received)</td>
        <td>Python</td>
    </tr>
    <tr>
        <td>17</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/8uqtpm/my_whatsapp_incoming_and_outgoing_message_count/">My WhatsApp Incoming and Outgoing Message Count since 2012</a></td>
        <td>* Density plot (x=Hour of the day, height=Number of messages)</td>
        <td>Python, Chart.js</td>
    </tr>
    <tr>
        <td>35</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/83m11s/group_chat_statistics_oc/">Group chat statistics</a></td>
        <td>Super nice - have a look at it!</td>
        <td>R</td>
    </tr>
    <tr>
        <td>2</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/8x1tdc/top_10_emojis_from_my_incoming_and_outgoing/">Top 10 Emojis from my Incoming and Outgoing WhatsApp Messages since 2012</a></td>
        <td>* Line chart</td>
        <td>Python, Chart.js</td>
    </tr>
    <tr>
        <td></td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/82z6yk/probability_of_being_the_first_to_reply_per/">Probability of being the first to reply per person in a group chat</a></td>
        <td></td>
        <td>R,&nbsp;circlize</td>
    </tr>
    <tr>
        <td>17</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/9qjr5p/oc_we_just_broke_up_after_1_year_and_it_hurts_our/">1 year WhatsApp history</a></td>
        <td>* Word cloud</td>
        <td>https://anteateranalytics.com/whatsapp</td>
    </tr>
    <tr>
        <td>43</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/9v5okd/a_healthy_breakup_seen_through_whatsapp_history_oc/">A healthy break-up seen through WhatsApp history</a></td>
        <td>* Bar charts</td>
        <td></td>
    </tr>
    <tr>
        <td>80</td>
        <td><a href="https://www.reddit.com/r/dataisbeautiful/comments/99qbqf/kiss_emojis_sent_during_two_month_fling_with_a/">Kiss emojis sent</a></td>
        <td></td>
        <td></td>
    </tr>
</table>

## My analysis

* weekday/weekend cycles: http://www.climate-lab-book.ac.uk/spirals/


