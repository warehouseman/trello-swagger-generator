#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Constants
swagger = {
      "parameters": []
}

test_values = []
test_values.append("""
<li><strong>Arguments</strong>
  <ul>
    <li><code class="docutils literal"><span class="pre">idCustomSticker</span></code> (required)
      <ul>
        <li><strong>Valid Values:</strong> An id</li>
      </ul>
    </li>
  </ul>
</li>
""")
test_values.append("""
<li><strong>Arguments</strong>
  <ul>
    <li><code class="docutils literal"><span class="pre">name</span></code> (required)
      <ul>
        <li><strong>Valid Values:</strong> a string with a length from <code class="docutils literal"><span class="pre">0</span></code> to <code class="docutils literal"><span class="pre">16384</span></code></li>
      </ul>
    </li>
    <li><code class="docutils literal"><span class="pre">color</span></code> (required)
      <ul>
        <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,closed,idOrganization,pinned</span></code></li>
        <li><strong>Valid Values:</strong> A valid label color or <code class="docutils literal"><span class="pre">null</span></code></li>
      </ul>
    </li>
    <li><code class="docutils literal"><span class="pre">idBoard</span></code> (optional)
      <ul>
        <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
        <li><strong>Valid Values:</strong> An id</li>
      </ul>
    </li>
  </ul>
</li>
""")


