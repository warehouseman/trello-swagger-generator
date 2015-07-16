#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Constants
swagger = {
  "paths": {
    "pth": {
      "mthd": {
       "parameters": []
      }
    }
  },
  "definitions": {
  }
}

cursor = {'entity' : 'ent', 'path' : 'pth', 'method' : 'mthd'}

test_values = []
test_values.append("""
<li><code class="docutils literal"><span class="pre">idCustomSticker</span></code> (required)
  <ul>
    <li><strong>Valid Values:</strong> An id</li>
  </ul>
</li>
""")
test_values.append("""

<li><code class="docutils literal"><span class="pre">fields</span></code> (optional)
  <ul>
    <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,closed,idOrganization,pinned</span></code></li>
    <li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:
      <ul>
        <li><code class="docutils literal"><span class="pre">scaled</span></code></li>
        <li><code class="docutils literal"><span class="pre">url</span></code></li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li><code class="docutils literal"><span class="pre">fields</span></code> (optional)
  <ul>
    <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
    <li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:
      <ul>
        <li><code class="docutils literal"><span class="pre">color</span></code></li>
        <li><code class="docutils literal"><span class="pre">idBoard</span></code></li>
        <li><code class="docutils literal"><span class="pre">name</span></code></li>
        <li><code class="docutils literal"><span class="pre">uses</span></code></li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li>
  <code class="docutils literal"><span class="pre">entities</span></code>
  (optional)

  <ul>
    <li><strong>Default:</strong> <code class="docutils literal"><span class=
    "pre">false</span></code></li>

    <li>
      <strong>Valid Values:</strong>

      <ul>
        <li><code class="docutils literal"><span class=
        "pre">true</span></code></li>

        <li><code class="docutils literal"><span class=
        "pre">false</span></code></li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li>
  <code class="docutils literal"><span class="pre">display</span></code>(optional)
  <ul>
    <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
    <li>
      <strong>Valid Values:</strong>
      <ul>
        <li><code class="docutils literal"><span class="pre">true</span></code></li>
        <li><code class="docutils literal"><span class="pre">false</span></code></li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li>
  <code class="docutils literal"><span class="pre">format</span></code>
  (optional)

  <ul>
    <li><strong>Default:</strong> <code class="docutils literal"><span class=
    "pre">list</span></code></li>

    <li>
      <strong>Valid Values:</strong> One of:

      <ul>
        <li><code class="docutils literal"><span class=
        "pre">count</span></code></li>

        <li><code class="docutils literal"><span class=
        "pre">list</span></code></li>

        <li><code class="docutils literal"><span class=
        "pre">minimal</span></code></li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li><code class="docutils literal"><span class="pre">name</span></code> (required)
  <ul>
    <li><strong>Valid Values:</strong> a string with a length from <code class="docutils literal"><span class="pre">0</span></code> to <code class="docutils literal"><span class="pre">16384</span></code></li>
  </ul>
</li>
""")


