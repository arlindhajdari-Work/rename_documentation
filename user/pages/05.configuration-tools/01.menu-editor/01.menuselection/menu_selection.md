---
title: 'Menu Selection'
metadata:
    description: 'Menu system than what we inherited from vtiger CRM'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    limit: 5
    order:
        by: date
        dir: desc
    pagination: true
    url_taxonomy_filters: true
taxonomy:
    category:
        - course
    tag:
        - certification
---

coreBOS needs a better, more flexible menu system than what we inherited
from coreBOS CRM. So we set out to look for some options with some of
these goals in mind:

-   Dropdown menu system fully configurable by the user
-   Multilevel sub-menus
-   Support for multiple types of menu actions: module, url, separator
-   Fast loading
-   CSS based, ideally responsive

[SkeLa-](https://github.com/SkeLa-) has contributed three menu options
for coreBOS. One based on KendoUI, anther based on JQuery and another
based on pure HTML5/CSS following [Lightning Design
System](https://www.lightningdesignsystem.com) guidelines.

I evaluated all three options and decided to incorporate the Lightning
Design System menu. There were basically three main reasons for this
decision:

1.  I really like how it looks: clean, simple, professional. LDS
    guidelines in general are VERY sane, very well thought out and I
    would like to recommend them in the whole application in due time,
    so seeing this menu system enforced my position on this point.
2.  I am currently in a mind set to stay away from libraries. I want to
    use pure HTML5, CSS and Javascript wherever possible
3.  Load timing. Being pure HTML5/CSS this menu just wins hands down on
    the other two.

\*\* time in miliseconds to load the menu\*\*

<table class="table table-striped">
<th></th>
<th>jquery</th>
<th>LDS (1)</th>
<th>KendoUI</th>
<th>LDS (2)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>108,8</td>
<td>38,55</td>
<td>425,5</td>
<td>59,3</td>
</tr>
<tr class="even">
<td></td>
<td>73,3</td>
<td>15,05</td>
<td>413,5</td>
<td>20,6</td>
</tr>
<tr class="odd">
<td></td>
<td>42,5</td>
<td>66,14</td>
<td>384,5</td>
<td>35,9</td>
</tr>
<tr class="even">
<td></td>
<td>72,9</td>
<td>43,84</td>
<td>436,8</td>
<td>14,46</td>
</tr>
<tr class="odd">
<td></td>
<td>58</td>
<td>44,94</td>
<td>399,5</td>
<td>39,47</td>
</tr>
<tr class="even">
<td></td>
<td>92</td>
<td>35,58</td>
<td>413,2</td>
<td>13,7</td>
</tr>
<tr class="odd">
<td></td>
<td>84,36</td>
<td>12,83</td>
<td>511,1</td>
<td>43,7</td>
</tr>
<tr class="even">
<td></td>
<td>38,97</td>
<td>36,24</td>
<td>408,5</td>
<td>24,7</td>
</tr>
<tr class="odd">
<td></td>
<td>135,28</td>
<td>27,9</td>
<td>415,2</td>
<td>20,3</td>
</tr>
<tr class="even">
<td></td>
<td>96,46</td>
<td>59,46</td>
<td>438,3</td>
<td>51,34</td>
</tr>
<tr class="odd">
<td><strong>Total:</strong></td>
<td>802,57</td>
<td>380,53</td>
<td>4246,1</td>
<td>323,47</td>
</tr>
<tr class="even">
<td><strong>Average:</strong></td>
<td>80,257</td>
<td><strong>38,053</strong></td>
<td>424,61</td>
<td><strong>32,347</strong></td>
</tr>
</tbody>
</table>

So, as of the end of December 2016, coreBOS now has an advanced menu
system based on Lightning Design System.

<div class="notices blue">
Thank you <a href="https://github.com/SkeLa-"> SkeLa!</a>
</div>

