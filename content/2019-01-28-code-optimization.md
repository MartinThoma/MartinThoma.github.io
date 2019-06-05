---
layout: post
title: Code Optimization
slug: code-optimization
author: Martin Thoma
date: 2019-01-28 20:00
category: Code
tags: Software Engineering, Productivity
featured_image: logos/python.png
---
Code optimization is about making programs run faster. In this article, I'll
give some basic ideas how to do it.

<div class="info">This article is NOT about <a href="https://martin-thoma.com/optimization-basics/">optimization problems</a>. It is also not about compression. Neither is it about churn rates (making users / companies happy).</div>

There is a ton of different ways how to speed up things. You can use algorithms
and data structures that scale better. You can avoid some operations
completely, because you actually don't use the results. Caching is also a
technique that quite often helps to avoid repeating costly operations. In some
cases it is completely fine to have computationally intensive parts, but you
want to pre-compute them. So maybe you can just change the point in time when
the costly operation is done.


## Scalability

You should know how your code scales. When you write a data structure, you
should document the Big-O notation of its operations. When you write functions,
you should do the same.

So much about nice an innocent thoughts. In reality, you probably get
distracted or simply have more important things to do than noting the runtime
complexity of your code. It's clear anyway, right?

The truth is between those extremes. You should always look for potential
scalability issues. In contrast to programming challenges, you have only a
vague idea about the size of the inputs. Then rather assume an order of
magnitude too much than too little. And think about in which direction you
have to scale: More calls or calls with bigger arguments?


## Measuring Performance

Measuring performance has two aspects: Profiling the overall program to find
which parts most time is spend on and then improving that part. For profiling
in Python, I use `cProfile`. For improving I compare solutions via `timeit`.

### cProfile

Create a profile:

```
$ python -m cProfile -o profile_output your_script.py
```

View the profile in a web browser:

```
$ cprofilev -f profile_output
```


### timeit

You might wonder for two solutions which one is the faster one. While this can
be incredible hard to answer for arbitary hardware, even for your machine with
roughly the same load it is a tough question. You need to execute the stuff
multiple times, have the same setup (to make sure that the same stuff is
cached) and then look at the measured results.

For example, take the question [Fastest way to count non spacing chars in Unicode text in Python](https://stackoverflow.com/q/54345897/562769) with the following solutions:

```
import timeit
import sys
import unicodedata
import numpy as np

UNICODE_NSM = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B', '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D', '\u031E', '\u031F', '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335', '\u0336', '\u0337', '\u0338', '\u0339', '\u033A', '\u033B', '\u033C', '\u033D', '\u033E', '\u033F', '\u0340', '\u0341', '\u0342', '\u0343', '\u0344', '\u0345', '\u0346', '\u0347', '\u0348', '\u0349', '\u034A', '\u034B', '\u034C', '\u034D', '\u034E', '\u034F', '\u0350', '\u0351', '\u0352', '\u0353', '\u0354', '\u0355', '\u0356', '\u0357', '\u0358', '\u0359', '\u035A', '\u035B', '\u035C', '\u035D', '\u035E', '\u035F', '\u0360', '\u0361', '\u0362', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036A', '\u036B', '\u036C', '\u036D', '\u036E', '\u036F', '\u0483', '\u0484', '\u0485', '\u0486', '\u0487', '\u0591', '\u0592', '\u0593', '\u0594', '\u0595', '\u0596', '\u0597', '\u0598', '\u0599', '\u059A', '\u059B', '\u059C', '\u059D', '\u059E', '\u059F', '\u05A0', '\u05A1', '\u05A2', '\u05A3', '\u05A4', '\u05A5', '\u05A6', '\u05A7', '\u05A8', '\u05A9', '\u05AA', '\u05AB', '\u05AC', '\u05AD', '\u05AE', '\u05AF', '\u05B0', '\u05B1', '\u05B2', '\u05B3', '\u05B4', '\u05B5', '\u05B6', '\u05B7', '\u05B8', '\u05B9', '\u05BA', '\u05BB', '\u05BC', '\u05BD', '\u05BF', '\u05C1', '\u05C2', '\u05C4', '\u05C5', '\u05C7', '\u0610', '\u0611', '\u0612', '\u0613', '\u0614', '\u0615', '\u0616', '\u0617', '\u0618', '\u0619', '\u061A', '\u064B', '\u064C', '\u064D', '\u064E', '\u064F', '\u0650', '\u0651', '\u0652', '\u0653', '\u0654', '\u0655', '\u0656', '\u0657', '\u0658', '\u0659', '\u065A', '\u065B', '\u065C', '\u065D', '\u065E', '\u065F', '\u0670', '\u06D6', '\u06D7', '\u06D8', '\u06D9', '\u06DA', '\u06DB', '\u06DC', '\u06DF', '\u06E0', '\u06E1', '\u06E2', '\u06E3', '\u06E4', '\u06E7', '\u06E8', '\u06EA', '\u06EB', '\u06EC', '\u06ED', '\u0711', '\u0730', '\u0731', '\u0732', '\u0733', '\u0734', '\u0735', '\u0736', '\u0737', '\u0738', '\u0739', '\u073A', '\u073B', '\u073C', '\u073D', '\u073E', '\u073F', '\u0740', '\u0741', '\u0742', '\u0743', '\u0744', '\u0745', '\u0746', '\u0747', '\u0748', '\u0749', '\u074A', '\u07A6', '\u07A7', '\u07A8', '\u07A9', '\u07AA', '\u07AB', '\u07AC', '\u07AD', '\u07AE', '\u07AF', '\u07B0', '\u07EB', '\u07EC', '\u07ED', '\u07EE', '\u07EF', '\u07F0', '\u07F1', '\u07F2', '\u07F3', '\u0816', '\u0817', '\u0818', '\u0819', '\u081B', '\u081C', '\u081D', '\u081E', '\u081F', '\u0820', '\u0821', '\u0822', '\u0823', '\u0825', '\u0826', '\u0827', '\u0829', '\u082A', '\u082B', '\u082C', '\u082D', '\u0859', '\u085A', '\u085B', '\u08E4', '\u08E5', '\u08E6', '\u08E7', '\u08E8', '\u08E9', '\u08EA', '\u08EB', '\u08EC', '\u08ED', '\u08EE', '\u08EF', '\u08F0', '\u08F1', '\u08F2', '\u08F3', '\u08F4', '\u08F5', '\u08F6', '\u08F7', '\u08F8', '\u08F9', '\u08FA', '\u08FB', '\u08FC', '\u08FD', '\u08FE', '\u0900', '\u0901', '\u0902', '\u093A', '\u093C', '\u093E', '\u0941', '\u0942', '\u0943', '\u0944', '\u0945', '\u0946', '\u0947', '\u0948', '\u094D', '\u0951', '\u0952', '\u0953', '\u0954', '\u0955', '\u0956', '\u0957', '\u0962', '\u0963', '\u0981', '\u09BC', '\u09C1', '\u09C2', '\u09C3', '\u09C4', '\u09CD', '\u09E2', '\u09E3', '\u0A01', '\u0A02', '\u0A3C', '\u0A41', '\u0A42', '\u0A47', '\u0A48', '\u0A4B', '\u0A4C', '\u0A4D', '\u0A51', '\u0A70', '\u0A71', '\u0A75', '\u0A81', '\u0A82', '\u0ABC', '\u0AC1', '\u0AC2', '\u0AC3', '\u0AC4', '\u0AC5', '\u0AC7', '\u0AC8', '\u0ACD', '\u0AE2', '\u0AE3', '\u0B01', '\u0B3C', '\u0B3F', '\u0B41', '\u0B42', '\u0B43', '\u0B44', '\u0B4D', '\u0B56', '\u0B62', '\u0B63', '\u0B82', '\u0BC0', '\u0BCD', '\u0C3E', '\u0C3F', '\u0C40', '\u0C46', '\u0C47', '\u0C48', '\u0C4A', '\u0C4B', '\u0C4C', '\u0C4D', '\u0C55', '\u0C56', '\u0C62', '\u0C63', '\u0CBC', '\u0CBF', '\u0CC6', '\u0CCC', '\u0CCD', '\u0CE2', '\u0CE3', '\u0D41', '\u0D42', '\u0D43', '\u0D44', '\u0D4D', '\u0D62', '\u0D63', '\u0DCA', '\u0DD2', '\u0DD3', '\u0DD4', '\u0DD6', '\u0E31', '\u0E34', '\u0E35', '\u0E36', '\u0E37', '\u0E38', '\u0E39', '\u0E3A', '\u0E47', '\u0E48', '\u0E49', '\u0E4A', '\u0E4B', '\u0E4C', '\u0E4D', '\u0E4E', '\u0EB1', '\u0EB4', '\u0EB5', '\u0EB6', '\u0EB7', '\u0EB8', '\u0EB9', '\u0EBB', '\u0EBC', '\u0EC8', '\u0EC9', '\u0ECA', '\u0ECB', '\u0ECC', '\u0ECD', '\u0F18', '\u0F19', '\u0F35', '\u0F37', '\u0F39', '\u0F71', '\u0F72', '\u0F73', '\u0F74', '\u0F75', '\u0F76', '\u0F77', '\u0F78', '\u0F79', '\u0F7A', '\u0F7B', '\u0F7C', '\u0F7D', '\u0F7E', '\u0F80', '\u0F81', '\u0F82', '\u0F83', '\u0F84', '\u0F86', '\u0F87', '\u0F8D', '\u0F8E', '\u0F8F', '\u0F90', '\u0F91', '\u0F92', '\u0F93', '\u0F94', '\u0F95', '\u0F96', '\u0F97', '\u0F99', '\u0F9A', '\u0F9B', '\u0F9C', '\u0F9D', '\u0F9E', '\u0F9F', '\u0FA0', '\u0FA1', '\u0FA2', '\u0FA3', '\u0FA4', '\u0FA5', '\u0FA6', '\u0FA7', '\u0FA8', '\u0FA9', '\u0FAA', '\u0FAB', '\u0FAC', '\u0FAD', '\u0FAE', '\u0FAF', '\u0FB0', '\u0FB1', '\u0FB2', '\u0FB3', '\u0FB4', '\u0FB5', '\u0FB6', '\u0FB7', '\u0FB8', '\u0FB9', '\u0FBA', '\u0FBB', '\u0FBC', '\u0FC6', '\u102D', '\u102E', '\u102F', '\u1030', '\u1032', '\u1033', '\u1034', '\u1035', '\u1036', '\u1037', '\u1039', '\u103A', '\u103D', '\u103E', '\u1058', '\u1059', '\u105E', '\u105F', '\u1060', '\u1071', '\u1072', '\u1073', '\u1074', '\u1082', '\u1085', '\u1086', '\u108D', '\u109D', '\u135D', '\u135E', '\u135F', '\u1712', '\u1713', '\u1714', '\u1732', '\u1733', '\u1734', '\u1752', '\u1753', '\u1772', '\u1773', '\u17B4', '\u17B5', '\u17B7', '\u17B8', '\u17B9', '\u17BA', '\u17BB', '\u17BC', '\u17BD', '\u17C6', '\u17C9', '\u17CA', '\u17CB', '\u17CC', '\u17CD', '\u17CE', '\u17CF', '\u17D0', '\u17D1', '\u17D2', '\u17D3', '\u17DD', '\u180B', '\u180C', '\u180D', '\u18A9', '\u1920', '\u1921', '\u1922', '\u1927', '\u1928', '\u1932', '\u1939', '\u193A', '\u193B', '\u1A17', '\u1A18', '\u1A56', '\u1A58', '\u1A59', '\u1A5A', '\u1A5B', '\u1A5C', '\u1A5D', '\u1A5E', '\u1A60', '\u1A62', '\u1A65', '\u1A66', '\u1A67', '\u1A68', '\u1A69', '\u1A6A', '\u1A6B', '\u1A6C', '\u1A73', '\u1A74', '\u1A75', '\u1A76', '\u1A77', '\u1A78', '\u1A79', '\u1A7A', '\u1A7B', '\u1A7C', '\u1A7F', '\u1B00', '\u1B01', '\u1B02', '\u1B03', '\u1B34', '\u1B36', '\u1B37', '\u1B38', '\u1B39', '\u1B3A', '\u1B3C', '\u1B42', '\u1B6B', '\u1B6C', '\u1B6D', '\u1B6E', '\u1B6F', '\u1B70', '\u1B71', '\u1B72', '\u1B73', '\u1B80', '\u1B81', '\u1BA2', '\u1BA3', '\u1BA4', '\u1BA5', '\u1BA8', '\u1BA9', '\u1BAB', '\u1BE6', '\u1BE8', '\u1BE9', '\u1BED', '\u1BEF', '\u1BF0', '\u1BF1', '\u1C2C', '\u1C2D', '\u1C2E', '\u1C2F', '\u1C30', '\u1C31', '\u1C32', '\u1C33', '\u1C36', '\u1C37', '\u1CD0', '\u1CD1', '\u1CD2', '\u1CD4', '\u1CD5', '\u1CD6', '\u1CD7', '\u1CD8', '\u1CD9', '\u1CDA', '\u1CDB', '\u1CDC', '\u1CDD', '\u1CDE', '\u1CDF', '\u1CE0', '\u1CE2', '\u1CE3', '\u1CE4', '\u1CE5', '\u1CE6', '\u1CE7', '\u1CE8', '\u1CED', '\u1CF4', '\u1DC0', '\u1DC1', '\u1DC2', '\u1DC3', '\u1DC4', '\u1DC5', '\u1DC6', '\u1DC7', '\u1DC8', '\u1DC9', '\u1DCA', '\u1DCB', '\u1DCC', '\u1DCD', '\u1DCE', '\u1DCF', '\u1DD0', '\u1DD1', '\u1DD2', '\u1DD3', '\u1DD4', '\u1DD5', '\u1DD6', '\u1DD7', '\u1DD8', '\u1DD9', '\u1DDA', '\u1DDB', '\u1DDC', '\u1DDD', '\u1DDE', '\u1DDF', '\u1DE0', '\u1DE1', '\u1DE2', '\u1DE3', '\u1DE4', '\u1DE5', '\u1DE6', '\u1DFC', '\u1DFD', '\u1DFE', '\u1DFF', '\u20D0', '\u20D1', '\u20D2', '\u20D3', '\u20D4', '\u20D5', '\u20D6', '\u20D7', '\u20D8', '\u20D9', '\u20DA', '\u20DB', '\u20DC', '\u20E1', '\u20E5', '\u20E6', '\u20E7', '\u20E8', '\u20E9', '\u20EA', '\u20EB', '\u20EC', '\u20ED', '\u20EE', '\u20EF', '\u20F0', '\u2CEF', '\u2CF0', '\u2CF1', '\u2D7F', '\u2DE0', '\u2DE1', '\u2DE2', '\u2DE3', '\u2DE4', '\u2DE5', '\u2DE6', '\u2DE7', '\u2DE8', '\u2DE9', '\u2DEA', '\u2DEB', '\u2DEC', '\u2DED', '\u2DEE', '\u2DEF', '\u2DF0', '\u2DF1', '\u2DF2', '\u2DF3', '\u2DF4', '\u2DF5', '\u2DF6', '\u2DF7', '\u2DF8', '\u2DF9', '\u2DFA', '\u2DFB', '\u2DFC', '\u2DFD', '\u2DFE', '\u2DFF', '\u302A', '\u302B', '\u302C', '\u302D', '\u3099', '\u309A', '\uA66F', '\uA674', '\uA675', '\uA676', '\uA677', '\uA678', '\uA679', '\uA67A', '\uA67B', '\uA67C', '\uA67D', '\uA69F', '\uA6F0', '\uA6F1', '\uA802', '\uA806', '\uA80B', '\uA825', '\uA826', '\uA8C4', '\uA8E0', '\uA8E1', '\uA8E2', '\uA8E3', '\uA8E4', '\uA8E5', '\uA8E6', '\uA8E7', '\uA8E8', '\uA8E9', '\uA8EA', '\uA8EB', '\uA8EC', '\uA8ED', '\uA8EE', '\uA8EF', '\uA8F0', '\uA8F1', '\uA926', '\uA927', '\uA928', '\uA929', '\uA92A', '\uA92B', '\uA92C', '\uA92D', '\uA947', '\uA948', '\uA949', '\uA94A', '\uA94B', '\uA94C', '\uA94D', '\uA94E', '\uA94F', '\uA950', '\uA951', '\uA980', '\uA981', '\uA982', '\uA9B3', '\uA9B6', '\uA9B7', '\uA9B8', '\uA9B9', '\uA9BC', '\uAA29', '\uAA2A', '\uAA2B', '\uAA2C', '\uAA2D', '\uAA2E', '\uAA31', '\uAA32', '\uAA35', '\uAA36', '\uAA43', '\uAA4C', '\uAAB0', '\uAAB2', '\uAAB3', '\uAAB4', '\uAAB7', '\uAAB8', '\uAABE', '\uAABF', '\uAAC1', '\uAAEC', '\uAAED', '\uAAF6', '\uABE5', '\uABE8', '\uABED', '\uFB1E', '\uFE00', '\uFE01', '\uFE02', '\uFE03', '\uFE04', '\uFE05', '\uFE06', '\uFE07', '\uFE08', '\uFE09', '\uFE0A', '\uFE0B', '\uFE0C', '\uFE0D', '\uFE0E', '\uFE0F', '\uFE20', '\uFE21', '\uFE22', '\uFE23', '\uFE24', '\uFE25', '\uFE26', '\U000101FD', '\U00010A01', '\U00010A02', '\U00010A03', '\U00010A05', '\U00010A06', '\U00010A0C', '\U00010A0D', '\U00010A0E', '\U00010A0F', '\U00010A38', '\U00010A39', '\U00010A3A', '\U00010A3F', '\U00011001', '\U00011038', '\U00011039', '\U0001103A', '\U0001103B', '\U0001103C', '\U0001103D', '\U0001103E', '\U0001103F', '\U00011040', '\U00011041', '\U00011042', '\U00011043', '\U00011044', '\U00011045', '\U00011046', '\U00011080', '\U00011081', '\U000110B3', '\U000110B4', '\U000110B5', '\U000110B6', '\U000110B9', '\U000110BA', '\U00011100', '\U00011101', '\U00011102', '\U00011127', '\U00011128', '\U00011129', '\U0001112A', '\U0001112B', '\U0001112D', '\U0001112E', '\U0001112F', '\U00011130', '\U00011131', '\U00011132', '\U00011133', '\U00011134', '\U00011180', '\U00011181', '\U000111B6', '\U000111B7', '\U000111B8', '\U000111B9', '\U000111BA', '\U000111BB', '\U000111BC', '\U000111BD', '\U000111BE', '\U000116AB', '\U000116AD', '\U000116B0', '\U000116B1', '\U000116B2', '\U000116B3', '\U000116B4', '\U000116B5', '\U000116B7', '\U00016F8F', '\U00016F90', '\U00016F91', '\U00016F92', '\U0001D167', '\U0001D168', '\U0001D169', '\U0001D17B', '\U0001D17C', '\U0001D17D', '\U0001D17E', '\U0001D17F', '\U0001D180', '\U0001D181', '\U0001D182', '\U0001D185', '\U0001D186', '\U0001D187', '\U0001D188', '\U0001D189', '\U0001D18A', '\U0001D18B', '\U0001D1AA', '\U0001D1AB', '\U0001D1AC', '\U0001D1AD', '\U0001D242', '\U0001D243', '\U0001D244', '\U000E0100', '\U000E0101', '\U000E0102', '\U000E0103', '\U000E0104', '\U000E0105', '\U000E0106', '\U000E0107', '\U000E0108', '\U000E0109', '\U000E010A', '\U000E010B', '\U000E010C', '\U000E010D', '\U000E010E', '\U000E010F', '\U000E0110', '\U000E0111', '\U000E0112', '\U000E0113', '\U000E0114', '\U000E0115', '\U000E0116', '\U000E0117', '\U000E0118', '\U000E0119', '\U000E011A', '\U000E011B', '\U000E011C', '\U000E011D', '\U000E011E', '\U000E011F', '\U000E0120', '\U000E0121', '\U000E0122', '\U000E0123', '\U000E0124', '\U000E0125', '\U000E0126', '\U000E0127', '\U000E0128', '\U000E0129', '\U000E012A', '\U000E012B', '\uE012C', '\U000E012D', '\U000E012E', '\U000E012F', '\U000E0130', '\U000E0131', '\U000E0132', '\U000E0133', '\U000E0134', '\U000E0135', '\U000E0136', '\U000E0137', '\U000E0138', '\U000E0139', '\U000E013A', '\U000E013B', '\U000E013C', '\U000E013D', '\U000E013E', '\U000E013F', '\U000E0140', '\U000E0141', '\U000E0142', '\U000E0143', '\U000E0144', '\U000E0145', '\U000E0146', '\U000E0147', '\U000E0148', '\U000E0149', '\U000E014A', '\U000E014B', '\U000E014C', '\U000E014D', '\U000E014E', '\U000E014F', '\U000E0150', '\U000E0151', '\U000E0152', '\U000E0153', '\U000E0154', '\U000E0155', '\U000E0156', '\U000E0157', '\U000E0158', '\U000E0159', '\U000E015A', '\U000E015B', '\U000E015C', '\U000E015D', '\U000E015E', '\U000E015F', '\U000E0160', '\U000E0161', '\U000E0162', '\U000E0163', '\U000E0164', '\U000E0165', '\U000E0166', '\U000E0167', '\U000E0168', '\U000E0169', '\U000E016A', '\U000E016B', '\U000E016C', '\U000E016D', '\U000E016E', '\U000E016F', '\U000E0170', '\U000E0171', '\U000E0172', '\U000E0173', '\U000E0174', '\U000E0175', '\U000E0176', '\U000E0177', '\U000E0178', '\U000E0179', '\U000E017A', '\U000E017B', '\U000E017C', '\U000E017D', '\U000E017E', '\U000E017F', '\U000E0180', '\U000E0181', '\U000E0182', '\U000E0183', '\U000E0184', '\U000E0185', '\uE0186', '\U000E0187', '\U000E0188', '\U000E0189', '\U000E018A', '\U000E018B', '\U000E018C', '\U000E018D', '\U000E018E', '\U000E018F', '\U000E0190', '\U000E0191', '\U000E0192', '\U000E0193', '\U000E0194', '\U000E0195', '\U000E0196', '\U000E0197', '\U000E0198', '\U000E0199', '\U000E019A', '\U000E019B', '\U000E019C', '\U000E019D', '\U000E019E', '\U000E019F', '\U000E01A0', '\U000E01A1', '\U000E01A2', '\U000E01A3', '\U000E01A4', '\U000E01A5', '\U000E01A6', '\U000E01A7', '\U000E01A8', '\U000E01A9', '\U000E01AA', '\U000E01AB', '\U000E01AC', '\U000E01AD', '\U000E01AE', '\U000E01AF', '\U000E01B0', '\U000E01B1', '\U000E01B2', '\U000E01B3', '\U000E01B4', '\U000E01B5', '\U000E01B6', '\U000E01B7', '\U000E01B8', '\U000E01B9', '\U000E01BA', '\U000E01BB', '\U000E01BC', '\U000E01BD', '\U000E01BE', '\U000E01BF', '\U000E01C0', '\U000E01C1', '\U000E01C2', '\U000E01C3', '\U000E01C4', '\U000E01C5', '\U000E01C6', '\U000E01C7', '\U000E01C8', '\U000E01C9', '\U000E01CA', '\U000E01CB', '\U000E01CC', '\U000E01CD', '\U000E01CE', '\U000E01CF', '\U000E01D0', '\U000E01D1', '\U000E01D2', '\U000E01D3', '\U000E01D4', '\U000E01D5', '\U000E01D6', '\U000E01D7', '\U000E01D8', '\U000E01D9', '\U000E01DA', '\U000E01DB', '\U000E01DC', '\U000E01DD', '\U000E01DE', '\U000E01DF', '\U000E01E0', '\U000E01E1', '\U000E01E2', '\U000E01E3', '\U000E01E4', '\U000E01E5', '\U000E01E6', '\U000E01E7', '\U000E01E8', '\U000E01E9', '\U000E01EA', '\U000E01EB', '\U000E01EC', '\U000E01ED', '\U000E01EE', '\U000E01EF']
MARK_SET = set(chr(c) for c in range(sys.maxunicode + 1) if unicodedata.category(chr(c))[0] == 'M')

def generator_count(text):
    return sum(1 for char in text if char not in UNICODE_NSM)


def loop_count(text):
    # 1769137
    count = 0
    for char in text:
        if char not in UNICODE_NSM:
            count += 1
    return count


def markset_count(text):
    return sum(char not in MARK_SET for char in text)


def category_count(text):
    return sum(unicodedata.category(char) != 'Mn' for char in text)
```

Besides the fact that two make a list-lookups and the other two make set lookups,
it might be hard to tell how much of a difference that makes. So I took
[a big text file](https://github.com/loretoparisi/unicode_marks/blob/master/UnicodeData.txt) for
comparison and used `timeit`. As different runs have different times, I counted
a couple of them and created [Box plots](https://en.wikipedia.org/wiki/Box_plot)
to show the distribution of execution times. I also made sure that the algorithm
is correct (never forget that when you optimize code!).

```
import timeit
import sys
import unicodedata
import numpy as np

UNICODE_NSM = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B', '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D', '\u031E', '\u031F', '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335', '\u0336', '\u0337', '\u0338', '\u0339', '\u033A', '\u033B', '\u033C', '\u033D', '\u033E', '\u033F', '\u0340', '\u0341', '\u0342', '\u0343', '\u0344', '\u0345', '\u0346', '\u0347', '\u0348', '\u0349', '\u034A', '\u034B', '\u034C', '\u034D', '\u034E', '\u034F', '\u0350', '\u0351', '\u0352', '\u0353', '\u0354', '\u0355', '\u0356', '\u0357', '\u0358', '\u0359', '\u035A', '\u035B', '\u035C', '\u035D', '\u035E', '\u035F', '\u0360', '\u0361', '\u0362', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036A', '\u036B', '\u036C', '\u036D', '\u036E', '\u036F', '\u0483', '\u0484', '\u0485', '\u0486', '\u0487', '\u0591', '\u0592', '\u0593', '\u0594', '\u0595', '\u0596', '\u0597', '\u0598', '\u0599', '\u059A', '\u059B', '\u059C', '\u059D', '\u059E', '\u059F', '\u05A0', '\u05A1', '\u05A2', '\u05A3', '\u05A4', '\u05A5', '\u05A6', '\u05A7', '\u05A8', '\u05A9', '\u05AA', '\u05AB', '\u05AC', '\u05AD', '\u05AE', '\u05AF', '\u05B0', '\u05B1', '\u05B2', '\u05B3', '\u05B4', '\u05B5', '\u05B6', '\u05B7', '\u05B8', '\u05B9', '\u05BA', '\u05BB', '\u05BC', '\u05BD', '\u05BF', '\u05C1', '\u05C2', '\u05C4', '\u05C5', '\u05C7', '\u0610', '\u0611', '\u0612', '\u0613', '\u0614', '\u0615', '\u0616', '\u0617', '\u0618', '\u0619', '\u061A', '\u064B', '\u064C', '\u064D', '\u064E', '\u064F', '\u0650', '\u0651', '\u0652', '\u0653', '\u0654', '\u0655', '\u0656', '\u0657', '\u0658', '\u0659', '\u065A', '\u065B', '\u065C', '\u065D', '\u065E', '\u065F', '\u0670', '\u06D6', '\u06D7', '\u06D8', '\u06D9', '\u06DA', '\u06DB', '\u06DC', '\u06DF', '\u06E0', '\u06E1', '\u06E2', '\u06E3', '\u06E4', '\u06E7', '\u06E8', '\u06EA', '\u06EB', '\u06EC', '\u06ED', '\u0711', '\u0730', '\u0731', '\u0732', '\u0733', '\u0734', '\u0735', '\u0736', '\u0737', '\u0738', '\u0739', '\u073A', '\u073B', '\u073C', '\u073D', '\u073E', '\u073F', '\u0740', '\u0741', '\u0742', '\u0743', '\u0744', '\u0745', '\u0746', '\u0747', '\u0748', '\u0749', '\u074A', '\u07A6', '\u07A7', '\u07A8', '\u07A9', '\u07AA', '\u07AB', '\u07AC', '\u07AD', '\u07AE', '\u07AF', '\u07B0', '\u07EB', '\u07EC', '\u07ED', '\u07EE', '\u07EF', '\u07F0', '\u07F1', '\u07F2', '\u07F3', '\u0816', '\u0817', '\u0818', '\u0819', '\u081B', '\u081C', '\u081D', '\u081E', '\u081F', '\u0820', '\u0821', '\u0822', '\u0823', '\u0825', '\u0826', '\u0827', '\u0829', '\u082A', '\u082B', '\u082C', '\u082D', '\u0859', '\u085A', '\u085B', '\u08E4', '\u08E5', '\u08E6', '\u08E7', '\u08E8', '\u08E9', '\u08EA', '\u08EB', '\u08EC', '\u08ED', '\u08EE', '\u08EF', '\u08F0', '\u08F1', '\u08F2', '\u08F3', '\u08F4', '\u08F5', '\u08F6', '\u08F7', '\u08F8', '\u08F9', '\u08FA', '\u08FB', '\u08FC', '\u08FD', '\u08FE', '\u0900', '\u0901', '\u0902', '\u093A', '\u093C', '\u093E', '\u0941', '\u0942', '\u0943', '\u0944', '\u0945', '\u0946', '\u0947', '\u0948', '\u094D', '\u0951', '\u0952', '\u0953', '\u0954', '\u0955', '\u0956', '\u0957', '\u0962', '\u0963', '\u0981', '\u09BC', '\u09C1', '\u09C2', '\u09C3', '\u09C4', '\u09CD', '\u09E2', '\u09E3', '\u0A01', '\u0A02', '\u0A3C', '\u0A41', '\u0A42', '\u0A47', '\u0A48', '\u0A4B', '\u0A4C', '\u0A4D', '\u0A51', '\u0A70', '\u0A71', '\u0A75', '\u0A81', '\u0A82', '\u0ABC', '\u0AC1', '\u0AC2', '\u0AC3', '\u0AC4', '\u0AC5', '\u0AC7', '\u0AC8', '\u0ACD', '\u0AE2', '\u0AE3', '\u0B01', '\u0B3C', '\u0B3F', '\u0B41', '\u0B42', '\u0B43', '\u0B44', '\u0B4D', '\u0B56', '\u0B62', '\u0B63', '\u0B82', '\u0BC0', '\u0BCD', '\u0C3E', '\u0C3F', '\u0C40', '\u0C46', '\u0C47', '\u0C48', '\u0C4A', '\u0C4B', '\u0C4C', '\u0C4D', '\u0C55', '\u0C56', '\u0C62', '\u0C63', '\u0CBC', '\u0CBF', '\u0CC6', '\u0CCC', '\u0CCD', '\u0CE2', '\u0CE3', '\u0D41', '\u0D42', '\u0D43', '\u0D44', '\u0D4D', '\u0D62', '\u0D63', '\u0DCA', '\u0DD2', '\u0DD3', '\u0DD4', '\u0DD6', '\u0E31', '\u0E34', '\u0E35', '\u0E36', '\u0E37', '\u0E38', '\u0E39', '\u0E3A', '\u0E47', '\u0E48', '\u0E49', '\u0E4A', '\u0E4B', '\u0E4C', '\u0E4D', '\u0E4E', '\u0EB1', '\u0EB4', '\u0EB5', '\u0EB6', '\u0EB7', '\u0EB8', '\u0EB9', '\u0EBB', '\u0EBC', '\u0EC8', '\u0EC9', '\u0ECA', '\u0ECB', '\u0ECC', '\u0ECD', '\u0F18', '\u0F19', '\u0F35', '\u0F37', '\u0F39', '\u0F71', '\u0F72', '\u0F73', '\u0F74', '\u0F75', '\u0F76', '\u0F77', '\u0F78', '\u0F79', '\u0F7A', '\u0F7B', '\u0F7C', '\u0F7D', '\u0F7E', '\u0F80', '\u0F81', '\u0F82', '\u0F83', '\u0F84', '\u0F86', '\u0F87', '\u0F8D', '\u0F8E', '\u0F8F', '\u0F90', '\u0F91', '\u0F92', '\u0F93', '\u0F94', '\u0F95', '\u0F96', '\u0F97', '\u0F99', '\u0F9A', '\u0F9B', '\u0F9C', '\u0F9D', '\u0F9E', '\u0F9F', '\u0FA0', '\u0FA1', '\u0FA2', '\u0FA3', '\u0FA4', '\u0FA5', '\u0FA6', '\u0FA7', '\u0FA8', '\u0FA9', '\u0FAA', '\u0FAB', '\u0FAC', '\u0FAD', '\u0FAE', '\u0FAF', '\u0FB0', '\u0FB1', '\u0FB2', '\u0FB3', '\u0FB4', '\u0FB5', '\u0FB6', '\u0FB7', '\u0FB8', '\u0FB9', '\u0FBA', '\u0FBB', '\u0FBC', '\u0FC6', '\u102D', '\u102E', '\u102F', '\u1030', '\u1032', '\u1033', '\u1034', '\u1035', '\u1036', '\u1037', '\u1039', '\u103A', '\u103D', '\u103E', '\u1058', '\u1059', '\u105E', '\u105F', '\u1060', '\u1071', '\u1072', '\u1073', '\u1074', '\u1082', '\u1085', '\u1086', '\u108D', '\u109D', '\u135D', '\u135E', '\u135F', '\u1712', '\u1713', '\u1714', '\u1732', '\u1733', '\u1734', '\u1752', '\u1753', '\u1772', '\u1773', '\u17B4', '\u17B5', '\u17B7', '\u17B8', '\u17B9', '\u17BA', '\u17BB', '\u17BC', '\u17BD', '\u17C6', '\u17C9', '\u17CA', '\u17CB', '\u17CC', '\u17CD', '\u17CE', '\u17CF', '\u17D0', '\u17D1', '\u17D2', '\u17D3', '\u17DD', '\u180B', '\u180C', '\u180D', '\u18A9', '\u1920', '\u1921', '\u1922', '\u1927', '\u1928', '\u1932', '\u1939', '\u193A', '\u193B', '\u1A17', '\u1A18', '\u1A56', '\u1A58', '\u1A59', '\u1A5A', '\u1A5B', '\u1A5C', '\u1A5D', '\u1A5E', '\u1A60', '\u1A62', '\u1A65', '\u1A66', '\u1A67', '\u1A68', '\u1A69', '\u1A6A', '\u1A6B', '\u1A6C', '\u1A73', '\u1A74', '\u1A75', '\u1A76', '\u1A77', '\u1A78', '\u1A79', '\u1A7A', '\u1A7B', '\u1A7C', '\u1A7F', '\u1B00', '\u1B01', '\u1B02', '\u1B03', '\u1B34', '\u1B36', '\u1B37', '\u1B38', '\u1B39', '\u1B3A', '\u1B3C', '\u1B42', '\u1B6B', '\u1B6C', '\u1B6D', '\u1B6E', '\u1B6F', '\u1B70', '\u1B71', '\u1B72', '\u1B73', '\u1B80', '\u1B81', '\u1BA2', '\u1BA3', '\u1BA4', '\u1BA5', '\u1BA8', '\u1BA9', '\u1BAB', '\u1BE6', '\u1BE8', '\u1BE9', '\u1BED', '\u1BEF', '\u1BF0', '\u1BF1', '\u1C2C', '\u1C2D', '\u1C2E', '\u1C2F', '\u1C30', '\u1C31', '\u1C32', '\u1C33', '\u1C36', '\u1C37', '\u1CD0', '\u1CD1', '\u1CD2', '\u1CD4', '\u1CD5', '\u1CD6', '\u1CD7', '\u1CD8', '\u1CD9', '\u1CDA', '\u1CDB', '\u1CDC', '\u1CDD', '\u1CDE', '\u1CDF', '\u1CE0', '\u1CE2', '\u1CE3', '\u1CE4', '\u1CE5', '\u1CE6', '\u1CE7', '\u1CE8', '\u1CED', '\u1CF4', '\u1DC0', '\u1DC1', '\u1DC2', '\u1DC3', '\u1DC4', '\u1DC5', '\u1DC6', '\u1DC7', '\u1DC8', '\u1DC9', '\u1DCA', '\u1DCB', '\u1DCC', '\u1DCD', '\u1DCE', '\u1DCF', '\u1DD0', '\u1DD1', '\u1DD2', '\u1DD3', '\u1DD4', '\u1DD5', '\u1DD6', '\u1DD7', '\u1DD8', '\u1DD9', '\u1DDA', '\u1DDB', '\u1DDC', '\u1DDD', '\u1DDE', '\u1DDF', '\u1DE0', '\u1DE1', '\u1DE2', '\u1DE3', '\u1DE4', '\u1DE5', '\u1DE6', '\u1DFC', '\u1DFD', '\u1DFE', '\u1DFF', '\u20D0', '\u20D1', '\u20D2', '\u20D3', '\u20D4', '\u20D5', '\u20D6', '\u20D7', '\u20D8', '\u20D9', '\u20DA', '\u20DB', '\u20DC', '\u20E1', '\u20E5', '\u20E6', '\u20E7', '\u20E8', '\u20E9', '\u20EA', '\u20EB', '\u20EC', '\u20ED', '\u20EE', '\u20EF', '\u20F0', '\u2CEF', '\u2CF0', '\u2CF1', '\u2D7F', '\u2DE0', '\u2DE1', '\u2DE2', '\u2DE3', '\u2DE4', '\u2DE5', '\u2DE6', '\u2DE7', '\u2DE8', '\u2DE9', '\u2DEA', '\u2DEB', '\u2DEC', '\u2DED', '\u2DEE', '\u2DEF', '\u2DF0', '\u2DF1', '\u2DF2', '\u2DF3', '\u2DF4', '\u2DF5', '\u2DF6', '\u2DF7', '\u2DF8', '\u2DF9', '\u2DFA', '\u2DFB', '\u2DFC', '\u2DFD', '\u2DFE', '\u2DFF', '\u302A', '\u302B', '\u302C', '\u302D', '\u3099', '\u309A', '\uA66F', '\uA674', '\uA675', '\uA676', '\uA677', '\uA678', '\uA679', '\uA67A', '\uA67B', '\uA67C', '\uA67D', '\uA69F', '\uA6F0', '\uA6F1', '\uA802', '\uA806', '\uA80B', '\uA825', '\uA826', '\uA8C4', '\uA8E0', '\uA8E1', '\uA8E2', '\uA8E3', '\uA8E4', '\uA8E5', '\uA8E6', '\uA8E7', '\uA8E8', '\uA8E9', '\uA8EA', '\uA8EB', '\uA8EC', '\uA8ED', '\uA8EE', '\uA8EF', '\uA8F0', '\uA8F1', '\uA926', '\uA927', '\uA928', '\uA929', '\uA92A', '\uA92B', '\uA92C', '\uA92D', '\uA947', '\uA948', '\uA949', '\uA94A', '\uA94B', '\uA94C', '\uA94D', '\uA94E', '\uA94F', '\uA950', '\uA951', '\uA980', '\uA981', '\uA982', '\uA9B3', '\uA9B6', '\uA9B7', '\uA9B8', '\uA9B9', '\uA9BC', '\uAA29', '\uAA2A', '\uAA2B', '\uAA2C', '\uAA2D', '\uAA2E', '\uAA31', '\uAA32', '\uAA35', '\uAA36', '\uAA43', '\uAA4C', '\uAAB0', '\uAAB2', '\uAAB3', '\uAAB4', '\uAAB7', '\uAAB8', '\uAABE', '\uAABF', '\uAAC1', '\uAAEC', '\uAAED', '\uAAF6', '\uABE5', '\uABE8', '\uABED', '\uFB1E', '\uFE00', '\uFE01', '\uFE02', '\uFE03', '\uFE04', '\uFE05', '\uFE06', '\uFE07', '\uFE08', '\uFE09', '\uFE0A', '\uFE0B', '\uFE0C', '\uFE0D', '\uFE0E', '\uFE0F', '\uFE20', '\uFE21', '\uFE22', '\uFE23', '\uFE24', '\uFE25', '\uFE26', '\U000101FD', '\U00010A01', '\U00010A02', '\U00010A03', '\U00010A05', '\U00010A06', '\U00010A0C', '\U00010A0D', '\U00010A0E', '\U00010A0F', '\U00010A38', '\U00010A39', '\U00010A3A', '\U00010A3F', '\U00011001', '\U00011038', '\U00011039', '\U0001103A', '\U0001103B', '\U0001103C', '\U0001103D', '\U0001103E', '\U0001103F', '\U00011040', '\U00011041', '\U00011042', '\U00011043', '\U00011044', '\U00011045', '\U00011046', '\U00011080', '\U00011081', '\U000110B3', '\U000110B4', '\U000110B5', '\U000110B6', '\U000110B9', '\U000110BA', '\U00011100', '\U00011101', '\U00011102', '\U00011127', '\U00011128', '\U00011129', '\U0001112A', '\U0001112B', '\U0001112D', '\U0001112E', '\U0001112F', '\U00011130', '\U00011131', '\U00011132', '\U00011133', '\U00011134', '\U00011180', '\U00011181', '\U000111B6', '\U000111B7', '\U000111B8', '\U000111B9', '\U000111BA', '\U000111BB', '\U000111BC', '\U000111BD', '\U000111BE', '\U000116AB', '\U000116AD', '\U000116B0', '\U000116B1', '\U000116B2', '\U000116B3', '\U000116B4', '\U000116B5', '\U000116B7', '\U00016F8F', '\U00016F90', '\U00016F91', '\U00016F92', '\U0001D167', '\U0001D168', '\U0001D169', '\U0001D17B', '\U0001D17C', '\U0001D17D', '\U0001D17E', '\U0001D17F', '\U0001D180', '\U0001D181', '\U0001D182', '\U0001D185', '\U0001D186', '\U0001D187', '\U0001D188', '\U0001D189', '\U0001D18A', '\U0001D18B', '\U0001D1AA', '\U0001D1AB', '\U0001D1AC', '\U0001D1AD', '\U0001D242', '\U0001D243', '\U0001D244', '\U000E0100', '\U000E0101', '\U000E0102', '\U000E0103', '\U000E0104', '\U000E0105', '\U000E0106', '\U000E0107', '\U000E0108', '\U000E0109', '\U000E010A', '\U000E010B', '\U000E010C', '\U000E010D', '\U000E010E', '\U000E010F', '\U000E0110', '\U000E0111', '\U000E0112', '\U000E0113', '\U000E0114', '\U000E0115', '\U000E0116', '\U000E0117', '\U000E0118', '\U000E0119', '\U000E011A', '\U000E011B', '\U000E011C', '\U000E011D', '\U000E011E', '\U000E011F', '\U000E0120', '\U000E0121', '\U000E0122', '\U000E0123', '\U000E0124', '\U000E0125', '\U000E0126', '\U000E0127', '\U000E0128', '\U000E0129', '\U000E012A', '\U000E012B', '\uE012C', '\U000E012D', '\U000E012E', '\U000E012F', '\U000E0130', '\U000E0131', '\U000E0132', '\U000E0133', '\U000E0134', '\U000E0135', '\U000E0136', '\U000E0137', '\U000E0138', '\U000E0139', '\U000E013A', '\U000E013B', '\U000E013C', '\U000E013D', '\U000E013E', '\U000E013F', '\U000E0140', '\U000E0141', '\U000E0142', '\U000E0143', '\U000E0144', '\U000E0145', '\U000E0146', '\U000E0147', '\U000E0148', '\U000E0149', '\U000E014A', '\U000E014B', '\U000E014C', '\U000E014D', '\U000E014E', '\U000E014F', '\U000E0150', '\U000E0151', '\U000E0152', '\U000E0153', '\U000E0154', '\U000E0155', '\U000E0156', '\U000E0157', '\U000E0158', '\U000E0159', '\U000E015A', '\U000E015B', '\U000E015C', '\U000E015D', '\U000E015E', '\U000E015F', '\U000E0160', '\U000E0161', '\U000E0162', '\U000E0163', '\U000E0164', '\U000E0165', '\U000E0166', '\U000E0167', '\U000E0168', '\U000E0169', '\U000E016A', '\U000E016B', '\U000E016C', '\U000E016D', '\U000E016E', '\U000E016F', '\U000E0170', '\U000E0171', '\U000E0172', '\U000E0173', '\U000E0174', '\U000E0175', '\U000E0176', '\U000E0177', '\U000E0178', '\U000E0179', '\U000E017A', '\U000E017B', '\U000E017C', '\U000E017D', '\U000E017E', '\U000E017F', '\U000E0180', '\U000E0181', '\U000E0182', '\U000E0183', '\U000E0184', '\U000E0185', '\uE0186', '\U000E0187', '\U000E0188', '\U000E0189', '\U000E018A', '\U000E018B', '\U000E018C', '\U000E018D', '\U000E018E', '\U000E018F', '\U000E0190', '\U000E0191', '\U000E0192', '\U000E0193', '\U000E0194', '\U000E0195', '\U000E0196', '\U000E0197', '\U000E0198', '\U000E0199', '\U000E019A', '\U000E019B', '\U000E019C', '\U000E019D', '\U000E019E', '\U000E019F', '\U000E01A0', '\U000E01A1', '\U000E01A2', '\U000E01A3', '\U000E01A4', '\U000E01A5', '\U000E01A6', '\U000E01A7', '\U000E01A8', '\U000E01A9', '\U000E01AA', '\U000E01AB', '\U000E01AC', '\U000E01AD', '\U000E01AE', '\U000E01AF', '\U000E01B0', '\U000E01B1', '\U000E01B2', '\U000E01B3', '\U000E01B4', '\U000E01B5', '\U000E01B6', '\U000E01B7', '\U000E01B8', '\U000E01B9', '\U000E01BA', '\U000E01BB', '\U000E01BC', '\U000E01BD', '\U000E01BE', '\U000E01BF', '\U000E01C0', '\U000E01C1', '\U000E01C2', '\U000E01C3', '\U000E01C4', '\U000E01C5', '\U000E01C6', '\U000E01C7', '\U000E01C8', '\U000E01C9', '\U000E01CA', '\U000E01CB', '\U000E01CC', '\U000E01CD', '\U000E01CE', '\U000E01CF', '\U000E01D0', '\U000E01D1', '\U000E01D2', '\U000E01D3', '\U000E01D4', '\U000E01D5', '\U000E01D6', '\U000E01D7', '\U000E01D8', '\U000E01D9', '\U000E01DA', '\U000E01DB', '\U000E01DC', '\U000E01DD', '\U000E01DE', '\U000E01DF', '\U000E01E0', '\U000E01E1', '\U000E01E2', '\U000E01E3', '\U000E01E4', '\U000E01E5', '\U000E01E6', '\U000E01E7', '\U000E01E8', '\U000E01E9', '\U000E01EA', '\U000E01EB', '\U000E01EC', '\U000E01ED', '\U000E01EE', '\U000E01EF']
MARK_SET = set(chr(c) for c in range(sys.maxunicode + 1) if unicodedata.category(chr(c))[0] == 'M')
print('len(UNICODE_NSM) = {}'.format(len(UNICODE_NSM)))
print('len(MARK_SET) = {}'.format(len(MARK_SET)))

filepath = "UnicodeData.txt"
with open(filepath) as f:
    text = f.read()


def main():
    ground_truth = loop_count(text)
    functions = [(loop_count, 'loop_count'),
                 (generator_count, 'generator_count'),
                 (category_count, 'category_count'),
                 (markset_count, 'markset_count'),
                 ]
    functions = functions[::-1]
    duration_list = {}
    for func, name in functions:
        is_correct = func(text) == ground_truth
        durations = timeit.repeat(lambda: func(text), repeat=500, number=3)
        if is_correct:
            correctness = 'correct'
        else:
            correctness = 'NOT correct'
        duration_list[name] = durations
        print('{func:<20}: {correctness}, '
              'min: {min:0.3f}s, mean: {mean:0.3f}s, max: {max:0.3f}s'
              .format(func=name,
                      correctness=correctness,
                      min=min(durations),
                      mean=np.mean(durations),
                      max=max(durations),
                      ))
        create_boxplot(duration_list)


def create_boxplot(duration_list):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import operator
    plt.figure(num=None, figsize=(8, 4), dpi=300,
               facecolor='w', edgecolor='k')
    sns.set(style="whitegrid")
    sorted_keys, sorted_vals = zip(*sorted(duration_list.items(), key=operator.itemgetter(1)))
    flierprops = dict(markerfacecolor='0.75', markersize=1,
                      linestyle='none')
    ax = sns.boxplot(data=sorted_vals, width=.3, orient='h',
                     flierprops=flierprops,)
    ax.set(xlabel="Time in s", ylabel="")
    plt.yticks(plt.yticks()[0], sorted_keys)
    plt.tight_layout()
    plt.savefig("output.png")
```

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/02/timeit-boxplot-4.png"><img src="../images/2019/02/timeit-boxplot-4.png" alt="Performance comparison of 4 algorithms." style="width: 512px;"/></a>
    <figcaption class="text-center">Performance comparison of 4 algorithms. The filled part of the four box-plots shows where 50% of the data is. The line in the middle of the filled part is the median.</figcaption>
</figure>

You can clearly see that the markset_count and the category_count are way
faster than the generator_count and the loop_count. Also the speed of the
latter two varies way more. Interestingly, the generator_count is slower than
the loop_count.

The markset_count is a bit faster than the category_count. I think that is the
case because looking up the category and doing the string comparison also takes
a bit of time. The difference is way more clear when you only plot the two and
increase the text length:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/02/timeit-boxplot-2.png"><img src="../images/2019/02/timeit-boxplot-2.png" alt="Performance comparison of markset_count and category_count." style="width: 512px;"/></a>
    <figcaption class="text-center">Performance comparison of markset_count and category_count.</figcaption>
</figure>



## Hints

* **Vectorization**: Gives the hell of a speedup. See [Vectorization and Parallelization in Python with Numpy and Pandas](https://datascience.blog.wzb.eu/2018/02/02/vectorization-and-parallelization-in-python-with-numpy-and-pandas/)
* **Immutable data structures**: Strings are often immutable (e.g. in Python).
  You might want to use a String Builder, in Python there is an article about
  [Efficient String Concatenation in Python](https://waymoot.org/home/python_string/)
* **Parallelization**: Again, a huge speedup is possible. My [Intel i7-6700HQ](https://ark.intel.com/content/www/us/en/ark/products/88967/intel-core-i7-6700hq-processor-6m-cache-up-to-3-50-ghz.html) allows 8 threads, so an 8x speedup is possible.


## Website Optimization

This is a super wide topic

See:

* [Optimizing Your Website with Jeff Atwood and Stackoverflow](https://hanselminutes.com/175/optimizing-your-website-with-jeff-atwood-and-stackoverflow)

## See also

* Wikipedia: [Program optimization](https://en.wikipedia.org/wiki/Program_optimization)
* Michael E. Lee: [Optimization of Computer Programs in C](http://icps.u-strasbg.fr/~bastoul/local_copies/lee.html)
