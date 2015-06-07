#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Constants
swagger = {
      "paths": {}
}

test_values = []
test_values.append("""
<div class="section" id="get-1-members-idmember-or-username">
  <h2>GET <span class="target" id="members-idmember-or-username">/1/members/[idMember or username]</span><a class="headerlink" href="https://trello.com/docs/api/member/index.html#get-1-members-idmember-or-username" title="Permalink to this headline">¶</a></h2>
  <ul class="simple">
    <li><strong>Notes:</strong> If you specify <code class="docutils literal"><span class="pre">me</span></code> as the username, this call will respond as if you had supplied the username associated with the supplied token</li>
    <li><strong>Required permissions:</strong> read</li>
    
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


    <li><strong>Examples</strong></li>
  </ul>
  <div class="highlight-URL">
    <div class="highlight">
      <pre>https://api.trello.com/1/members/bobtester?fields=username,fullName,url&amp;boards=all&amp;board_fields=name&amp;organizations=all&amp;organization_fields=displayName&amp;key=[application_key]&amp;token=[optional_auth_token]</pre>
    </div>
  </div>
  <div class="highlight-JavaScript">
    <div class="highlight">
      <pre>
        <span class="p">{</span>
        <span class="s2">"id"</span>
        <span class="o">:</span> <span class="s2">"4ee7df1be582acdec80000ae"</span><span class="p">,</span>
        <span class="s2">"username"</span><span class="o">:</span> <span class="s2">"bobtester"</span><span class="p">,</span>
        <span class="s2">"fullName"</span><span class="o">:</span> <span class="s2">"Bob Tester"</span><span class="p">,</span>
        <span class="s2">"url"</span><span class="o">:</span> <span class="s2">"https://trello.com/bobtester"</span><span class="p">,</span>
        <span class="s2">"organizations"</span><span class="o">:</span> <span class="p">[],</span>
        <span class="s2">"boards"</span><span class="o">:</span> <span class="p">[{</span>
            <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Example Board"</span><span class="p">,</span>
            <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4eea4ffc91e31d1746000046"</span>
        <span class="p">},</span> <span class="p">{</span>
            <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Public Board"</span><span class="p">,</span>
            <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4ee7e707e582acdec800051a"</span>
        <span class="p">}]</span> <span class="p">}</span>
      </pre>
    </div>
  </div>
</div>
""")
test_values.append("""
<div class="section" id="get-1-members-idmember-or-username">
  <h2>GET <span class="target" id="members-idmember-or-username">/1/members/[idMember or username]</span><a class="headerlink" href="https://trello.com/docs/api/member/index.html#get-1-members-idmember-or-username" title="Permalink to this headline">¶</a></h2>
  <ul class="simple">
    <li><strong>Notes:</strong> If you specify <code class="docutils literal"><span class="pre">me</span></code> as the username, this call will respond as if you had supplied the username associated with the supplied token</li>
    <li><strong>Required permissions:</strong> read</li>
    <li><strong>Arguments</strong>
      <ul>
        <li><code class="docutils literal"><span class="pre">XXXXXXX</span></code> (required)
          <ul>
            <li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,closed,idOrganization,pinned</span></code></li>
            <li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:
              <ul>
                <li><code class="docutils literal"><span class="pre">addAttachmentToCard</span></code></li>
                <li><code class="docutils literal"><span class="pre">addChecklistToCard</span></code></li>
              </ul>
            </li>
          </ul>
        </li>
        <li><code class="docutils literal"><span class="pre">actions</span></code> (optional)
          <ul>
            <li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:
              <ul>
                <li><code class="docutils literal"><span class="pre">addAttachmentToCard</span></code></li>
                <li><code class="docutils literal"><span class="pre">addChecklistToCard</span></code></li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </li>
    <li><strong>Examples</strong></li>
  </ul>
  <div class="highlight-URL">
    <div class="highlight">
      <pre>https://api.trello.com/1/members/bobtester?fields=username,fullName,url&amp;boards=all&amp;board_fields=name&amp;organizations=all&amp;organization_fields=displayName&amp;key=[application_key]&amp;token=[optional_auth_token]</pre>
    </div>
  </div>
  <div class="highlight-JavaScript">
    <div class="highlight">
      <pre>
        <span class="p">{</span>
        <span class="s2">"id"</span>
        <span class="o">:</span> <span class="s2">"4ee7df1be582acdec80000ae"</span><span class="p">,</span>
        <span class="s2">"username"</span><span class="o">:</span> <span class="s2">"bobtester"</span><span class="p">,</span>
        <span class="s2">"fullName"</span><span class="o">:</span> <span class="s2">"Bob Tester"</span><span class="p">,</span>
        <span class="s2">"url"</span><span class="o">:</span> <span class="s2">"https://trello.com/bobtester"</span><span class="p">,</span>
        <span class="s2">"organizations"</span><span class="o">:</span> <span class="p">[],</span>
        <span class="s2">"boards"</span><span class="o">:</span> <span class="p">[{</span>
            <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Example Board"</span><span class="p">,</span>
            <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4eea4ffc91e31d1746000046"</span>
        <span class="p">},</span> <span class="p">{</span>
            <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Public Board"</span><span class="p">,</span>
            <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4ee7e707e582acdec800051a"</span>
        <span class="p">}]</span> <span class="p">}</span>
      </pre>
    </div>
  </div>
</div>
""")
test_values.append("""
<div class="section" id="get-1-members-idmember-or-username">
<h2>GET <span class="target" id="members-idmember-or-username">/1/members/[idMember or username]</span><a class="headerlink" href="https://trello.com/docs/api/member/index.html#get-1-members-idmember-or-username" title="Permalink to this headline">¶</a></h2>
<ul class="simple">
<li><strong>Notes:</strong> If you specify <code class="docutils literal"><span class="pre">me</span></code> as the username, this call will respond as if you had supplied the username associated with the supplied token</li>
<li><strong>Required permissions:</strong> read</li>
<li><strong>Arguments</strong><ul>
<li><code class="docutils literal"><span class="pre">actions</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">addAttachmentToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addChecklistToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">addToOrganizationBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">commentCard</span></code></li>
<li><code class="docutils literal"><span class="pre">convertToCardFromCheckItem</span></code></li>
<li><code class="docutils literal"><span class="pre">copyBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">copyCard</span></code></li>
<li><code class="docutils literal"><span class="pre">copyCommentCard</span></code></li>
<li><code class="docutils literal"><span class="pre">createBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">createCard</span></code></li>
<li><code class="docutils literal"><span class="pre">createList</span></code></li>
<li><code class="docutils literal"><span class="pre">createOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteAttachmentFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteBoardInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteCard</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteOrganizationInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">disablePowerUp</span></code></li>
<li><code class="docutils literal"><span class="pre">emailCard</span></code></li>
<li><code class="docutils literal"><span class="pre">enablePowerUp</span></code></li>
<li><code class="docutils literal"><span class="pre">makeAdminOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">makeNormalMemberOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">makeNormalMemberOfOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">makeObserverOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">memberJoinedTrello</span></code></li>
<li><code class="docutils literal"><span class="pre">moveCardFromBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveCardToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveListFromBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveListToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeChecklistFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeFromOrganizationBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeMemberFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedBoardInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedOrganizationInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">updateBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:closed</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:desc</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:idList</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:name</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCheckItemStateOnCard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateChecklist</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList:closed</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList:name</span></code></li>
<li><code class="docutils literal"><span class="pre">updateMember</span></code></li>
<li><code class="docutils literal"><span class="pre">updateOrganization</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">actions_entities</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">actions_display</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">actions_limit</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">50</span></code></li>
<li><strong>Valid Values:</strong> a number from <code class="docutils literal"><span class="pre">0</span></code> to <code class="docutils literal"><span class="pre">1000</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">action_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">data</span></code></li>
<li><code class="docutils literal"><span class="pre">date</span></code></li>
<li><code class="docutils literal"><span class="pre">idMemberCreator</span></code></li>
<li><code class="docutils literal"><span class="pre">type</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">action_since</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> A date, <code class="docutils literal"><span class="pre">null</span></code> or <code class="docutils literal"><span class="pre">lastView</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">action_before</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> A date, or <code class="docutils literal"><span class="pre">null</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">cards</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
<li><code class="docutils literal"><span class="pre">open</span></code></li>
<li><code class="docutils literal"><span class="pre">visible</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">badges</span></code></li>
<li><code class="docutils literal"><span class="pre">checkItemStates</span></code></li>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">dateLastActivity</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">due</span></code></li>
<li><code class="docutils literal"><span class="pre">email</span></code></li>
<li><code class="docutils literal"><span class="pre">idAttachmentCover</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">idChecklists</span></code></li>
<li><code class="docutils literal"><span class="pre">idLabels</span></code></li>
<li><code class="docutils literal"><span class="pre">idList</span></code></li>
<li><code class="docutils literal"><span class="pre">idMembers</span></code></li>
<li><code class="docutils literal"><span class="pre">idMembersVoted</span></code></li>
<li><code class="docutils literal"><span class="pre">idShort</span></code></li>
<li><code class="docutils literal"><span class="pre">labels</span></code></li>
<li><code class="docutils literal"><span class="pre">manualCoverAttachment</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">pos</span></code></li>
<li><code class="docutils literal"><span class="pre">shortLink</span></code></li>
<li><code class="docutils literal"><span class="pre">shortUrl</span></code></li>
<li><code class="docutils literal"><span class="pre">subscribed</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_members</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_member_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">avatarHash,fullName,initials,username</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">avatarHash</span></code></li>
<li><code class="docutils literal"><span class="pre">bio</span></code></li>
<li><code class="docutils literal"><span class="pre">bioData</span></code></li>
<li><code class="docutils literal"><span class="pre">confirmed</span></code></li>
<li><code class="docutils literal"><span class="pre">fullName</span></code></li>
<li><code class="docutils literal"><span class="pre">idPremOrgsAdmin</span></code></li>
<li><code class="docutils literal"><span class="pre">initials</span></code></li>
<li><code class="docutils literal"><span class="pre">memberType</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">status</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">username</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_attachments</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong> A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_attachment_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">url,previews</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">bytes</span></code></li>
<li><code class="docutils literal"><span class="pre">date</span></code></li>
<li><code class="docutils literal"><span class="pre">edgeColor</span></code></li>
<li><code class="docutils literal"><span class="pre">idMember</span></code></li>
<li><code class="docutils literal"><span class="pre">isUpload</span></code></li>
<li><code class="docutils literal"><span class="pre">mimeType</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">previews</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">card_stickers</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">boards</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">members</span></code></li>
<li><code class="docutils literal"><span class="pre">open</span></code></li>
<li><code class="docutils literal"><span class="pre">organization</span></code></li>
<li><code class="docutils literal"><span class="pre">pinned</span></code></li>
<li><code class="docutils literal"><span class="pre">public</span></code></li>
<li><code class="docutils literal"><span class="pre">starred</span></code></li>
<li><code class="docutils literal"><span class="pre">unpinned</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,closed,idOrganization,pinned</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">dateLastActivity</span></code></li>
<li><code class="docutils literal"><span class="pre">dateLastView</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">idOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">invitations</span></code></li>
<li><code class="docutils literal"><span class="pre">invited</span></code></li>
<li><code class="docutils literal"><span class="pre">labelNames</span></code></li>
<li><code class="docutils literal"><span class="pre">memberships</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">pinned</span></code></li>
<li><code class="docutils literal"><span class="pre">powerUps</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">shortLink</span></code></li>
<li><code class="docutils literal"><span class="pre">shortUrl</span></code></li>
<li><code class="docutils literal"><span class="pre">starred</span></code></li>
<li><code class="docutils literal"><span class="pre">subscribed</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">addAttachmentToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addChecklistToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addMemberToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">addToOrganizationBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">commentCard</span></code></li>
<li><code class="docutils literal"><span class="pre">convertToCardFromCheckItem</span></code></li>
<li><code class="docutils literal"><span class="pre">copyBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">copyCard</span></code></li>
<li><code class="docutils literal"><span class="pre">copyCommentCard</span></code></li>
<li><code class="docutils literal"><span class="pre">createBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">createCard</span></code></li>
<li><code class="docutils literal"><span class="pre">createList</span></code></li>
<li><code class="docutils literal"><span class="pre">createOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteAttachmentFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteBoardInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteCard</span></code></li>
<li><code class="docutils literal"><span class="pre">deleteOrganizationInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">disablePowerUp</span></code></li>
<li><code class="docutils literal"><span class="pre">emailCard</span></code></li>
<li><code class="docutils literal"><span class="pre">enablePowerUp</span></code></li>
<li><code class="docutils literal"><span class="pre">makeAdminOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">makeNormalMemberOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">makeNormalMemberOfOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">makeObserverOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">memberJoinedTrello</span></code></li>
<li><code class="docutils literal"><span class="pre">moveCardFromBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveCardToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveListFromBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">moveListToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeChecklistFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeFromOrganizationBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">removeMemberFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedBoardInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedOrganizationInvitation</span></code></li>
<li><code class="docutils literal"><span class="pre">updateBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:closed</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:desc</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:idList</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCard:name</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCheckItemStateOnCard</span></code></li>
<li><code class="docutils literal"><span class="pre">updateChecklist</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList:closed</span></code></li>
<li><code class="docutils literal"><span class="pre">updateList:name</span></code></li>
<li><code class="docutils literal"><span class="pre">updateMember</span></code></li>
<li><code class="docutils literal"><span class="pre">updateOrganization</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions_entities</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions_display</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions_format</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">list</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">count</span></code></li>
<li><code class="docutils literal"><span class="pre">list</span></code></li>
<li><code class="docutils literal"><span class="pre">minimal</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions_since</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> A date, <code class="docutils literal"><span class="pre">null</span></code> or <code class="docutils literal"><span class="pre">lastView</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_actions_limit</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">50</span></code></li>
<li><strong>Valid Values:</strong> a number from <code class="docutils literal"><span class="pre">0</span></code> to <code class="docutils literal"><span class="pre">1000</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_action_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">data</span></code></li>
<li><code class="docutils literal"><span class="pre">date</span></code></li>
<li><code class="docutils literal"><span class="pre">idMemberCreator</span></code></li>
<li><code class="docutils literal"><span class="pre">type</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_lists</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
<li><code class="docutils literal"><span class="pre">open</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_memberships</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">active</span></code></li>
<li><code class="docutils literal"><span class="pre">admin</span></code></li>
<li><code class="docutils literal"><span class="pre">deactivated</span></code></li>
<li><code class="docutils literal"><span class="pre">me</span></code></li>
<li><code class="docutils literal"><span class="pre">normal</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_organization</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">board_organization_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,displayName</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">billableMemberCount</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">displayName</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoards</span></code></li>
<li><code class="docutils literal"><span class="pre">invitations</span></code></li>
<li><code class="docutils literal"><span class="pre">invited</span></code></li>
<li><code class="docutils literal"><span class="pre">logoHash</span></code></li>
<li><code class="docutils literal"><span class="pre">memberships</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">powerUps</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">premiumFeatures</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">website</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">boardsInvited</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">members</span></code></li>
<li><code class="docutils literal"><span class="pre">open</span></code></li>
<li><code class="docutils literal"><span class="pre">organization</span></code></li>
<li><code class="docutils literal"><span class="pre">pinned</span></code></li>
<li><code class="docutils literal"><span class="pre">public</span></code></li>
<li><code class="docutils literal"><span class="pre">starred</span></code></li>
<li><code class="docutils literal"><span class="pre">unpinned</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">boardsInvited_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">name,closed,idOrganization,pinned</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">closed</span></code></li>
<li><code class="docutils literal"><span class="pre">dateLastActivity</span></code></li>
<li><code class="docutils literal"><span class="pre">dateLastView</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">idOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">invitations</span></code></li>
<li><code class="docutils literal"><span class="pre">invited</span></code></li>
<li><code class="docutils literal"><span class="pre">labelNames</span></code></li>
<li><code class="docutils literal"><span class="pre">memberships</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">pinned</span></code></li>
<li><code class="docutils literal"><span class="pre">powerUps</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">shortLink</span></code></li>
<li><code class="docutils literal"><span class="pre">shortUrl</span></code></li>
<li><code class="docutils literal"><span class="pre">starred</span></code></li>
<li><code class="docutils literal"><span class="pre">subscribed</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">boardStars</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">savedSearches</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">organizations</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">members</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
<li><code class="docutils literal"><span class="pre">public</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">organization_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">billableMemberCount</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">displayName</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoards</span></code></li>
<li><code class="docutils literal"><span class="pre">invitations</span></code></li>
<li><code class="docutils literal"><span class="pre">invited</span></code></li>
<li><code class="docutils literal"><span class="pre">logoHash</span></code></li>
<li><code class="docutils literal"><span class="pre">memberships</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">powerUps</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">premiumFeatures</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">website</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">organization_paid_account</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">organizationsInvited</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">members</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
<li><code class="docutils literal"><span class="pre">public</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">organizationsInvited_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">billableMemberCount</span></code></li>
<li><code class="docutils literal"><span class="pre">desc</span></code></li>
<li><code class="docutils literal"><span class="pre">descData</span></code></li>
<li><code class="docutils literal"><span class="pre">displayName</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoards</span></code></li>
<li><code class="docutils literal"><span class="pre">invitations</span></code></li>
<li><code class="docutils literal"><span class="pre">invited</span></code></li>
<li><code class="docutils literal"><span class="pre">logoHash</span></code></li>
<li><code class="docutils literal"><span class="pre">memberships</span></code></li>
<li><code class="docutils literal"><span class="pre">name</span></code></li>
<li><code class="docutils literal"><span class="pre">powerUps</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">premiumFeatures</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">website</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notifications</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">addAdminToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">addAdminToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">addedAttachmentToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addedMemberToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addedToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">addedToCard</span></code></li>
<li><code class="docutils literal"><span class="pre">addedToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">cardDueSoon</span></code></li>
<li><code class="docutils literal"><span class="pre">changeCard</span></code></li>
<li><code class="docutils literal"><span class="pre">closeBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">commentCard</span></code></li>
<li><code class="docutils literal"><span class="pre">createdCard</span></code></li>
<li><code class="docutils literal"><span class="pre">declinedInvitationToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">declinedInvitationToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">invitedToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">invitedToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">makeAdminOfBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">makeAdminOfOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">memberJoinedTrello</span></code></li>
<li><code class="docutils literal"><span class="pre">mentionedOnCard</span></code></li>
<li><code class="docutils literal"><span class="pre">removedFromBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">removedFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">removedFromOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">removedMemberFromCard</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedInvitedToBoard</span></code></li>
<li><code class="docutils literal"><span class="pre">unconfirmedInvitedToOrganization</span></code></li>
<li><code class="docutils literal"><span class="pre">updateCheckItemStateOnCard</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notifications_entities</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notifications_display</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notifications_limit</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">50</span></code></li>
<li><strong>Valid Values:</strong> a number from <code class="docutils literal"><span class="pre">1</span></code> to <code class="docutils literal"><span class="pre">1000</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notification_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">data</span></code></li>
<li><code class="docutils literal"><span class="pre">date</span></code></li>
<li><code class="docutils literal"><span class="pre">idMemberCreator</span></code></li>
<li><code class="docutils literal"><span class="pre">type</span></code></li>
<li><code class="docutils literal"><span class="pre">unread</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notification_memberCreator</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">true</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notification_memberCreator_fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">avatarHash,fullName,initials,username</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">avatarHash</span></code></li>
<li><code class="docutils literal"><span class="pre">bio</span></code></li>
<li><code class="docutils literal"><span class="pre">bioData</span></code></li>
<li><code class="docutils literal"><span class="pre">confirmed</span></code></li>
<li><code class="docutils literal"><span class="pre">fullName</span></code></li>
<li><code class="docutils literal"><span class="pre">idPremOrgsAdmin</span></code></li>
<li><code class="docutils literal"><span class="pre">initials</span></code></li>
<li><code class="docutils literal"><span class="pre">memberType</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">status</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">username</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notification_before</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> An id, or <code class="docutils literal"><span class="pre">null</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">notification_since</span></code> (optional)<ul>
<li><strong>Valid Values:</strong> An id, or <code class="docutils literal"><span class="pre">null</span></code></li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">tokens</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">paid_account</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">false</span></code></li>
<li><strong>Valid Values:</strong><ul>
<li><code class="docutils literal"><span class="pre">true</span></code></li>
<li><code class="docutils literal"><span class="pre">false</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">boardBackgrounds</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">custom</span></code></li>
<li><code class="docutils literal"><span class="pre">default</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
<li><code class="docutils literal"><span class="pre">premium</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">customBoardBackgrounds</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">customStickers</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">customEmoji</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">none</span></code></li>
<li><strong>Valid Values:</strong> One of:<ul>
<li><code class="docutils literal"><span class="pre">all</span></code></li>
<li><code class="docutils literal"><span class="pre">none</span></code></li>
</ul>
</li>
</ul>
</li>
<li><code class="docutils literal"><span class="pre">fields</span></code> (optional)<ul>
<li><strong>Default:</strong> <code class="docutils literal"><span class="pre">all</span></code></li>
<li><strong>Valid Values:</strong> <code class="docutils literal"><span class="pre">all</span></code> or a comma-separated list of:<ul>
<li><code class="docutils literal"><span class="pre">avatarHash</span></code></li>
<li><code class="docutils literal"><span class="pre">avatarSource</span></code></li>
<li><code class="docutils literal"><span class="pre">bio</span></code></li>
<li><code class="docutils literal"><span class="pre">bioData</span></code></li>
<li><code class="docutils literal"><span class="pre">confirmed</span></code></li>
<li><code class="docutils literal"><span class="pre">email</span></code></li>
<li><code class="docutils literal"><span class="pre">fullName</span></code></li>
<li><code class="docutils literal"><span class="pre">gravatarHash</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoards</span></code></li>
<li><code class="docutils literal"><span class="pre">idBoardsPinned</span></code></li>
<li><code class="docutils literal"><span class="pre">idOrganizations</span></code></li>
<li><code class="docutils literal"><span class="pre">idPremOrgsAdmin</span></code></li>
<li><code class="docutils literal"><span class="pre">initials</span></code></li>
<li><code class="docutils literal"><span class="pre">loginTypes</span></code></li>
<li><code class="docutils literal"><span class="pre">memberType</span></code></li>
<li><code class="docutils literal"><span class="pre">oneTimeMessagesDismissed</span></code></li>
<li><code class="docutils literal"><span class="pre">prefs</span></code></li>
<li><code class="docutils literal"><span class="pre">premiumFeatures</span></code></li>
<li><code class="docutils literal"><span class="pre">products</span></code></li>
<li><code class="docutils literal"><span class="pre">status</span></code></li>
<li><code class="docutils literal"><span class="pre">status</span></code></li>
<li><code class="docutils literal"><span class="pre">trophies</span></code></li>
<li><code class="docutils literal"><span class="pre">uploadedAvatarHash</span></code></li>
<li><code class="docutils literal"><span class="pre">url</span></code></li>
<li><code class="docutils literal"><span class="pre">username</span></code></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><strong>Examples</strong></li>
</ul>
<div class="highlight-URL"><div class="highlight"><pre>https://api.trello.com/1/members/bobtester?fields=username,fullName,url&amp;boards=all&amp;board_fields=name&amp;organizations=all&amp;organization_fields=displayName&amp;key=[application_key]&amp;token=[optional_auth_token]
</pre></div>
</div>
<div class="highlight-JavaScript"><div class="highlight"><pre><span class="p">{</span>
  <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4ee7df1be582acdec80000ae"</span><span class="p">,</span>
  <span class="s2">"username"</span><span class="o">:</span> <span class="s2">"bobtester"</span><span class="p">,</span>
  <span class="s2">"fullName"</span><span class="o">:</span> <span class="s2">"Bob Tester"</span><span class="p">,</span>
  <span class="s2">"url"</span><span class="o">:</span> <span class="s2">"https://trello.com/bobtester"</span><span class="p">,</span>
  <span class="s2">"organizations"</span><span class="o">:</span> <span class="p">[],</span>
  <span class="s2">"boards"</span><span class="o">:</span> <span class="p">[{</span>
      <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Example Board"</span><span class="p">,</span>
      <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4eea4ffc91e31d1746000046"</span>
  <span class="p">},</span> <span class="p">{</span>
      <span class="s2">"name"</span><span class="o">:</span> <span class="s2">"Public Board"</span><span class="p">,</span>
      <span class="s2">"id"</span><span class="o">:</span> <span class="s2">"4ee7e707e582acdec800051a"</span>
  <span class="p">}]</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
""")

sampleAPI = """
{
  "swagger": "2.0",
  "info": {
    "description": "This is a sample server Petstore server.  You can find out more about Swagger at <a href='http:\/\/swagger.io'>http:\/\/swagger.io<\/a> or on irc.freenode.net, #swagger.  For this sample, you can use the api key 'special-key' to test the authorization filters",
    "version": "1.0.0",
    "title": "Swagger Petstore",
    "termsOfService": "http:\/\/helloreverb.com\/terms\/",
    "contact": {
      "email": "apiteam@swagger.io"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http:\/\/www.apache.org\/licenses\/LICENSE-2.0.html"
    }
  },
  "host": "petstore.swagger.io",
  "basePath": "\/v2",
  "tags": [
    {
      "name": "pet",
      "description": "Everything about your Pets",
      "externalDocs": {
        "description": "Find out more",
        "url": "http:\/\/swagger.io"
      }
    },
    {
      "name": "OneOfTheTrelloEntities",
      "description": "Access to Petstore orders"
    },
    {
      "name": "user",
      "description": "Operations about user",
      "externalDocs": {
        "description": "Find out more about our store",
        "url": "http:\/\/swagger.io"
      }
    }
  ],
  "schemes": [
    "http"
  ],
  "securityDefinitions": {
    "petstore_auth": {
      "type": "oauth2",
      "authorizationUrl": "http:\/\/petstore.swagger.io\/api\/oauth\/dialog",
      "flow": "implicit",
      "scopes": {
        "write:pets": "modify pets in your account",
        "read:pets": "read your pets"
      }
    },
    "api_key": {
      "type": "apiKey",
      "name": "api_key",
      "in": "header"
    }
  },
  "definitions": {
    "Order": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "petId": {
          "type": "integer",
          "format": "int64"
        },
        "quantity": {
          "type": "integer",
          "format": "int32"
        },
        "shipDate": {
          "type": "string",
          "format": "date-time"
        },
        "status": {
          "type": "string",
          "description": "Order Status",
          "enum": [
            "placed",
            "approved",
            "delivered"
          ]
        },
        "complete": {
          "type": "boolean",
          "default": false
        }
      },
      "xml": {
        "name": "Order"
      }
    },
    "Category": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Category"
      }
    },
    "User": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "username": {
          "type": "string"
        },
        "firstName": {
          "type": "string"
        },
        "lastName": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string"
        },
        "phone": {
          "type": "string"
        },
        "userStatus": {
          "type": "integer",
          "format": "int32",
          "description": "User Status"
        }
      },
      "xml": {
        "name": "User"
      }
    },
    "Tag": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Tag"
      }
    },
    "Pet": {
      "type": "object",
      "required": [
        "name",
        "photoUrls"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "category": {
          "$ref": "#\/definitions\/Category"
        },
        "name": {
          "type": "string",
          "example": "doggie"
        },
        "photoUrls": {
          "type": "array",
          "xml": {
            "name": "photoUrl",
            "wrapped": true
          },
          "items": {
            "type": "string"
          }
        },
        "tags": {
          "type": "array",
          "xml": {
            "name": "tag",
            "wrapped": true
          },
          "items": {
            "$ref": "#\/definitions\/Tag"
          }
        },
        "status": {
          "type": "string",
          "description": "pet status in the store",
          "enum": [
            "available",
            "pending",
            "sold"
          ]
        }
      },
      "xml": {
        "name": "Pet"
      }
    },
    "ApiResponse": {
      "type": "object",
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "type": {
          "type": "string"
        },
        "message": {
          "type": "string"
        }
      }
    }
  },
  "externalDocs": {
    "description": "Find out more about Swagger",
    "url": "http:\/\/swagger.io"
  }
}
"""

