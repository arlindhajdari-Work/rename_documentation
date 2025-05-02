---
title: 'Replacing prototype/scriptaculous with jQuery in coreBOS'
metadata:
    description: 'Replacing prototype/scriptaculous with jQuery in coreBOS'
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
        - development 
        - prototype2jquery
    tag:
        - howto
---

[Reference: Migrating from PrototypeJS to jQuery](https://andykdocs.de/development/JavaScript/Migrating+from+PrototypeJS+to+jQuery/#3-Events)

<table class="table table-striped">
<th>Event</th>
<th>Prototype</th>
<th>jQuery</th>
<th>Also recommended for coreBOS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Selecting DOM Elements</td>
<td><code class="sourceCode javascript">$(<span class="st">&#39;id&#39;</span>)</code></td>
<td><code class="sourceCode javascript">jQuery(<span class="st">&quot;#id&quot;</span>)</code></td>
<td><code class="sourceCode javascript"><span class="bu">document</span><span class="op">.</span><span class="fu">getElementById</span>(<span class="st">&quot;id&quot;</span>)</code></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript">$$(selector)[x]</code></td>
<td><code class="sourceCode javascript">jQuery(selector)<span class="op">.</span><span class="fu">eq</span>(x)</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript">$(element)<span class="op">.</span><span class="fu">select</span>( selector )</code></td>
<td><code class="sourceCode javascript">$(element)<span class="op">.</span><span class="fu">find</span>( selector )</code></td>
<td></td>
</tr>
<tr class="even">
<td>GET/SET content</td>
<td><code class="sourceCode javascript">$F(<span class="st">&#39;id&#39;</span>)</code></td>
<td><code class="sourceCode javascript">jQuery(<span class="st">&quot;#id&quot;</span>)<span class="op">.</span><span class="fu">val</span>()</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="at">innerHTML</span></code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">html</span>()</code></td>
<td><code class="sourceCode javascript"><span class="bu">document</span><span class="op">.</span><span class="fu">getElementById</span>(element)<span class="op">.</span><span class="at">innerHTML</span></code></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript">element<span class="op">.</span><span class="fu">update</span>(<span class="st">&#39;new content&#39;</span>)</code></td>
<td><code class="sourceCode javascript">element<span class="op">.</span><span class="fu">html</span>(<span class="st">&#39;new content&#39;</span>)<span class="op">;</span>
vtlib_executeJavascriptInElement(<span class="bu">document</span><span class="op">.</span><span class="fu">getElementById</span>(element))<span class="op">;</span></code></td>
<td><code class="sourceCode javascript"><span class="bu">document</span><span class="op">.</span><span class="fu">getElementById</span>(element)<span class="op">.</span><span class="at">innerHTML</span><span class="op">=</span><span class="st">&#39;new_content&#39;</span><span class="op">;</span>
vtlib_executeJavascriptInElement(<span class="bu">document</span><span class="op">.</span><span class="fu">getElementById</span>(element))<span class="op">;</span></code></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="at">value</span> <span class="op">=</span> x</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">val</span>(x)</code></td>
<td></td>
</tr>
<tr class="even">
<td>Update style</td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="at">style</span><span class="op">.</span><span class="at">x</span> <span class="op">=</span> <span class="st">&#39;y&#39;</span></code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">css</span>({ <span class="dt">x</span><span class="op">:</span> <span class="st">&#39;y&#39;</span> })</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">setStyle</span>( style(s) )</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">css</span>( propertyName<span class="op">,</span> value )</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">hasClassName</span>( className )</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">hasClass</span>( className )</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">addClassName</span>( className )</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">addClass</span>( className(s) )</code></td>
<td></td>
</tr>
<tr class="even">
<td>Get/Set Attributes</td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="at">checked</span></code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">prop</span>(<span class="st">&#39;checked&#39;</span>)</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript">disabled</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">prop</span>(<span class="st">&#39;disabled&#39;</span>)</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="at">some_attr</span></code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">attr</span>(<span class="st">&#39;some_attr&#39;</span>)</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">getWidth</span>()</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">width</span>()</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">empty</span>()</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">is</span>(<span class="st">&#39;:empty&#39;</span>)</code></td>
<td></td>
</tr>
<tr class="odd">
<td>Effects</td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">fade</span>({<span class="dt">duration</span><span class="op">:</span> x})</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">fadeOut</span>(x <span class="op">*</span> <span class="dv">1000</span>)</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">appear</span>({<span class="dt">duration</span><span class="op">:</span> x})</code></td>
<td><code class="sourceCode javascript"><span class="op">.</span><span class="fu">appear</span>({<span class="dt">duration</span><span class="op">:</span> x})</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Effect.Appear</td>
<td><code class="sourceCode javascript">fadeIn()</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Effect.Fade</td>
<td><code class="sourceCode javascript">fadeOut()</code></td>
<td></td>
</tr>
<tr class="odd">
<td>Event Handlers</td>
<td><code class="sourceCode javascript">$(element_id)<span class="op">.</span><span class="fu">observe</span>(<span class="st">&quot;click&quot;</span><span class="op">,</span>
 <span class="kw">function</span>(<span class="bu">event</span>){ <span class="op">...</span> })</code></td>
<td><code class="sourceCode javascript">jQuery(<span class="st">&#39;#&#39;</span><span class="op">+</span>element_id)<span class="op">.</span><span class="fu">bind</span>(<span class="st">&quot;click&quot;</span><span class="op">,</span>
 <span class="kw">function</span>(jQueryEvent){ <span class="op">...</span> })</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript"><span class="bu">document</span><span class="op">.</span><span class="fu">observe</span>(<span class="st">&quot;dom:loaded&quot;</span><span class="op">,</span>
 <span class="kw">function</span>() { <span class="op">...</span> })<span class="op">;</span></code></td>
<td><code class="sourceCode javascript">$(<span class="bu">document</span>)<span class="op">.</span><span class="fu">ready</span>()</code></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><code class="sourceCode javascript"><span class="bu">Event</span><span class="op">.</span><span class="fu">observe</span>(element<span class="op">,</span> eventName<span class="op">,</span> handler)</code></td>
<td><code class="sourceCode javascript">$(<span class="st">&#39;selector&#39;</span>)<span class="op">.</span><span class="fu">bind</span>(eventType<span class="op">,</span> handler)</code></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><code class="sourceCode javascript">Sortable<span class="op">.</span><span class="fu">create</span>(<span class="st">&quot;element&quot;</span> {
<span class="dt">constraint</span><span class="op">:</span><span class="kw">false</span><span class="op">,</span>
<span class="dt">tag</span><span class="op">:</span><span class="st">&#39;div&#39;</span><span class="op">,</span>
<span class="dt">overlap</span><span class="op">:</span><span class="st">&#39;Horizontal&#39;</span><span class="op">,</span>
<span class="dt">handle</span><span class="op">:</span><span class="st">&#39;headerrow&#39;</span><span class="op">,</span>
<span class="dt">onUpdate</span><span class="op">:</span><span class="kw">function</span>(){
<span class="co">// do smth</span>
}
})</code></td>
<td><code class="sourceCode javascript">jQuery(<span class="st">&quot;#element&quot;</span>)<span class="op">.</span><span class="fu">sortabe</span>({
<span class="dt">constraint</span><span class="op">:</span> <span class="kw">false</span><span class="op">,</span>
<span class="dt">tag</span><span class="op">:</span> <span class="st">&#39;div&#39;</span><span class="op">,</span>
<span class="dt">overlap</span><span class="op">:</span> <span class="st">&#39;Horizontal&#39;</span><span class="op">,</span>
<span class="dt">handle</span><span class="op">:</span> <span class="st">&#39;.headerrow&#39;</span><span class="op">,</span>
<span class="dt">update</span><span class="op">:</span> <span class="kw">function</span> () {
<span class="co">//do smth</span>
}
})</code></td>
<td></td>
</tr>
<tr class="odd">
<td>AJAX</td>
<td><code class="sourceCode javascript"><span class="kw">new</span> Ajax<span class="op">.</span><span class="fu">Request</span>(<span class="st">&#39;index.php&#39;</span><span class="op">,</span> {
<span class="dt">queue</span> <span class="op">:</span> {<span class="dt">position</span> <span class="op">:</span> <span class="st">&#39;end&#39;</span><span class="op">,</span>
<span class="dt">scope</span> <span class="op">:</span> <span class="st">&#39;command&#39;</span>}<span class="op">,</span>
<span class="dt">method</span> <span class="op">:</span> <span class="st">&#39;post&#39;</span><span class="op">,</span>
<span class="dt">postBody</span> <span class="op">:</span> <span class="st">&quot;urlstring&quot;</span><span class="op">,</span>
<span class="dt">onComplete</span> <span class="op">:</span> <span class="kw">function</span>(response) {
<span class="co">// do smth</span>
}
})<span class="op">;</span></code></td>
<td><code class="sourceCode javascript">jQuery<span class="op">.</span><span class="fu">ajax</span>({
<span class="dt">method</span><span class="op">:</span> <span class="st">&#39;POST&#39;</span><span class="op">,</span>
<span class="dt">url</span><span class="op">:</span><span class="st">&#39;urlstring&#39;</span><span class="op">,</span>
})<span class="op">.</span><span class="fu">done</span>(<span class="kw">function</span> (response) {
   <span class="co">//do smth</span>
})<span class="op">;</span></code></td>
<td></td>
</tr>
</tbody>
</table>
