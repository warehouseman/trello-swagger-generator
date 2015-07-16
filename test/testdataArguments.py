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
  }
}

cursor = {'entity' : 'ent', 'path' : 'pth', 'method' : 'mthd'}

pathFields = [{'idOrg': 'idOrg or name'}, {'field': 'field'}]

test_values = []
test_values.append("""
  <ul class="simple">
    <li><strong>Required permissions:</strong> read</li>

    <li>
      <strong>Arguments</strong>

      <ul>
        <li>
          <code class="docutils literal"><span class="pre">display</span></code>
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

        <li>
          <code class="docutils literal"><span class="pre">fields</span></code>
          (optional)

          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class=
            "pre">all</span></code></li>

            <li>
              <strong>Valid Values:</strong> <code class="docutils literal"><span class=
              "pre">all</span></code> or a comma-separated list of:

              <ul>
                <li><code class="docutils literal"><span class=
                "pre">data</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">date</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">idMemberCreator</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">type</span></code></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <code class="docutils literal"><span class="pre">member</span></code>
          (optional)

          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class=
            "pre">true</span></code></li>

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

        <li>
          <code class="docutils literal"><span class="pre">member_fields</span></code>
          (optional)

          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class=
            "pre">avatarHash,fullName,initials,username</span></code></li>

            <li>
              <strong>Valid Values:</strong> <code class="docutils literal"><span class=
              "pre">all</span></code> or a comma-separated list of:

              <ul>
                <li><code class="docutils literal"><span class=
                "pre">avatarHash</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">bio</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">bioData</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">confirmed</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">fullName</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">idPremOrgsAdmin</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">initials</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">memberType</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">products</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">status</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">url</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">username</span></code></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <code class="docutils literal"><span class="pre">memberCreator</span></code>
          (optional)

          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class=
            "pre">true</span></code></li>

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

        <li>
          <code class="docutils literal"><span class=
          "pre">memberCreator_fields</span></code> (optional)

          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class=
            "pre">avatarHash,fullName,initials,username</span></code></li>

            <li>
              <strong>Valid Values:</strong> <code class="docutils literal"><span class=
              "pre">all</span></code> or a comma-separated list of:

              <ul>
                <li><code class="docutils literal"><span class=
                "pre">avatarHash</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">bio</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">bioData</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">confirmed</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">fullName</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">idPremOrgsAdmin</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">initials</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">memberType</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">products</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">status</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">url</span></code></li>

                <li><code class="docutils literal"><span class=
                "pre">username</span></code></li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
""")

'''
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

'''
