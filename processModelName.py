#!/usr/bin/env python
import re

PATH_PATTERNS = []
PATH_EXTRACTOR = []
#  0
PATH_PATTERNS.append(re.compile('/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}_{}_{}".format(
  path.split('/')[1],
  path.split('/')[3],
  path.split('/')[5],
  path.split('/')[7]))

#  1
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}_{}_{}".format(
  path.split('/')[1],
  path.split('/')[3],
  path.split('/')[4].replace("{", "").replace("}", ""),
  path.split('/')[5]))

#  2
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}_{}".format(
  path.split('/')[1],
  path.split('/')[3],
  path.split('/')[5]))

#  3
PATH_PATTERNS.append(re.compile('/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/[a-zA-Z]+/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}".format(
  path.split('/')[3],
  path.split('/')[4]))

#  4
PATH_PATTERNS.append(re.compile('/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/{[a-zA-Z]+}$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}".format(
  path.split('/')[1],
  path.split('/')[3]))

#  5
PATH_PATTERNS.append(re.compile('/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}".format(
  path.split('/')[3],
  path.split('/')[4]))

#  6
PATH_PATTERNS.append(re.compile('/[a-zA-Z]+/{[a-zA-Z]+}/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: "{}_{}".format(
  path.split('/')[1],
  path.split('/')[3]))


#  7
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+/[a-zA-Z]+/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: path.split('/')[1])

#  8
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+/{[a-zA-Z]+}$'))
PATH_EXTRACTOR.append(lambda path: path.split('/')[1])

#  9
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+/$'))
PATH_EXTRACTOR.append(lambda path: path.split('/')[1])

# 10
PATH_PATTERNS.append(re.compile('^/[a-zA-Z]+$'))
PATH_EXTRACTOR.append(lambda path: path.split('/')[1])

debugPrint = False

#  Methods
def determineModelName(path):

  modelName = ''
  idx = 0
  for pattern in PATH_PATTERNS :
    if pattern.match(path) :
      modelName = PATH_EXTRACTOR[idx](path)
      if idx == -999 :
        print "<####  {} -- {} || {} ####>".format(idx, modelName, path)

    idx = idx+1

  return modelName

#  -   -   -   -   -   -   -   -   -   -   -
#  Main routine (for testing)
def main():

  paths = []
  paths.append('/boards/{idBoard}/prefs/background')
  paths.append('/boards/{idBoard}/prefs/calendarFeedEnabled')
  paths.append('/boards/{idBoard}/prefs/cardAging')
  paths.append('/boards/{idBoard}/prefs/cardCovers')
  paths.append('/boards/{idBoard}/prefs/comments')
  paths.append('/boards/{idBoard}/prefs/invitations')
  paths.append('/boards/{idBoard}/prefs/permissionLevel')
  paths.append('/boards/{idBoard}/prefs/selfJoin')
  paths.append('/boards/{idBoard}/prefs/voting')
  paths.append('/boards/{idBoard}/calendarKey/generate')
  paths.append('/boards/{idBoard}/labelNames/blue')
  paths.append('/boards/{idBoard}/labelNames/green')
  paths.append('/boards/{idBoard}/labelNames/orange')
  paths.append('/boards/{idBoard}/labelNames/purple')
  paths.append('/boards/{idBoard}/labelNames/red')
  paths.append('/boards/{idBoard}/labelNames/yellow')
  paths.append('/boards/{idBoard}/emailKey/generate')
  paths.append('/boards/{idBoard}/myPrefs/emailPosition')
  paths.append('/boards/{idBoard}/myPrefs/idEmailList')
  paths.append('/boards/{idBoard}/myPrefs/showListGuide')
  paths.append('/boards/{idBoard}/myPrefs/showSidebar')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarActivity')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarBoardActions')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarMembers')

  paths.append('/boards/{idBoard}/checklists')
  paths.append('/boards/{idBoard}/labels')
  paths.append('/boards/{idBoard}/lists')
  paths.append('/boards/{idBoard}/closed')
  paths.append('/boards/{idBoard}/desc')
  paths.append('/boards/{idBoard}/idOrganization')
  paths.append('/boards/{idBoard}/members')
  paths.append('/boards/{idBoard}/name')
  paths.append('/boards/{idBoard}/subscribed')
  paths.append('/boards/{idBoard}/markAsViewed')
  paths.append('/boards/{idBoard}/powerUps')

  paths.append('/boards/{idBoard}')

  paths.append('/boards')

  paths.append('/boards/{idBoard}/members/{idMember}')
  paths.append('/boards/{idBoard}/memberships/{idMembership}')
  paths.append('/boards/{idBoard}/members/{idMember}')
  paths.append('/boards/{idBoard}/powerUps/{powerUp}')

  paths.append('/actions/{idAction}')
  paths.append('/actions/{idAction}/text')
  paths.append('/actions/{idAction}')
  paths.append('/cards/{card}')
  paths.append('/cards/{card}/actions/{idAction}/comments')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem/{idCheckItem}/name')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem/{idCheckItem}/state')
  paths.append('/cards/{card}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem}')
  paths.append('/cards/{card}/closed')
  paths.append('/cards/{card}/desc')
  paths.append('/cards/{card}/due')
  paths.append('/cards/{card}/idAttachmentCover')
  paths.append('/cards/{card}/idBoard')
  paths.append('/cards/{card}/idList')
  paths.append('/cards/{card}/idMembers')
  paths.append('/cards/{card}/labels')
  paths.append('/cards/{card}/name')
  paths.append('/cards/{card}/pos')
  paths.append('/cards/{card}/stickers/{idSticker}')
  paths.append('/cards/{card}/subscribed')
  paths.append('/cards')
  paths.append('/cards/{card}/actions/comments')
  paths.append('/cards/{card}/attachments')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard')
  paths.append('/cards/{card}/checklists')
  paths.append('/cards/{card}/idLabels')
  paths.append('/cards/{card}/idMembers')
  paths.append('/cards/{card}/labels')
  paths.append('/cards/{card}/markAssociatedNotificationsRead')
  paths.append('/cards/{card}/membersVoted')
  paths.append('/cards/{card}/stickers')
  paths.append('/cards/{card}')
  paths.append('/cards/{card}/actions/{idAction}/comments')
  paths.append('/cards/{card}/attachments/{idAttachment}')
  paths.append('/cards/{card}/checklist/{idChecklist}/checkItem/{idCheckItem}')
  paths.append('/cards/{card}/checklists/{idChecklist}')
  paths.append('/cards/{card}/idLabels/{idLabel}')
  paths.append('/cards/{card}/idMembers/{idMember}')
  paths.append('/cards/{card}/labels/{color}')
  paths.append('/cards/{card}/membersVoted/{idMember}')
  paths.append('/cards/{card}/stickers/{idSticker}')
  paths.append('/checklists/{idChecklist}')
  paths.append('/checklists/{idChecklist}/idCard')
  paths.append('/checklists/{idChecklist}/name')
  paths.append('/checklists/{idChecklist}/pos')
  paths.append('/checklists')
  paths.append('/checklists/{idChecklist}/checkItems')
  paths.append('/checklists/{idChecklist}')
  paths.append('/checklists/{idChecklist}/checkItems/{idCheckItem}')
  paths.append('/labels/{idLabel}')
  paths.append('/labels/{idLabel}/color')
  paths.append('/labels/{idLabel}/name')
  paths.append('/labels')
  paths.append('/labels/{idLabel}')
  paths.append('/lists/{idList}')
  paths.append('/lists/{idList}/closed')
  paths.append('/lists/{idList}/idBoard')
  paths.append('/lists/{idList}/name')
  paths.append('/lists/{idList}/pos')
  paths.append('/lists/{idList}/subscribed')
  paths.append('/lists')
  paths.append('/lists/{idList}/archiveAllCards')
  paths.append('/lists/{idList}/cards')
  paths.append('/lists/{idList}/moveAllCards')
  paths.append('/members/{idMember}')
  paths.append('/members/{idMember}/avatarSource')
  paths.append('/members/{idMember}/bio')
  paths.append('/members/{idMember}/boardBackgrounds/{idBoardBackground}')
  paths.append('/members/{idMember}/boardStars/{idBoardStar}')
  paths.append('/members/{idMember}/boardStars/{idBoardStar}/idBoard')
  paths.append('/members/{idMember}/boardStars/{idBoardStar}/pos')
  paths.append('/members/{idMember}/customBoardBackgrounds/{idBoardBackground}')
  paths.append('/members/{idMember}/fullName')
  paths.append('/members/{idMember}/initials')
  paths.append('/members/{idMember}/prefs/colorBlind')
  paths.append('/members/{idMember}/prefs/locale')
  paths.append('/members/{idMember}/prefs/minutesBetweenSummaries')
  paths.append('/members/{idMember}/savedSearches/{idSavedSearch}')
  paths.append('/members/{idMember}/savedSearches/{idSavedSearch}/name')
  paths.append('/members/{idMember}/savedSearches/{idSavedSearch}/pos')
  paths.append('/members/{idMember}/savedSearches/{idSavedSearch}/query')
  paths.append('/members/{idMember}/username')
  paths.append('/members/{idMember}/avatar')
  paths.append('/members/{idMember}/boardBackgrounds')
  paths.append('/members/{idMember}/boardStars')
  paths.append('/members/{idMember}/customBoardBackgrounds')
  paths.append('/members/{idMember}/customEmoji')
  paths.append('/members/{idMember}/customStickers')
  paths.append('/members/{idMember}/oneTimeMessagesDismissed')
  paths.append('/members/{idMember}/savedSearches')
  paths.append('/members/{idMember}/boardBackgrounds/{idBoardBackground}')
  paths.append('/members/{idMember}/boardStars/{idBoardStar}')
  paths.append('/members/{idMember}/customBoardBackgrounds/{idBoardBackground}')
  paths.append('/members/{idMember}/customStickers/{idCustomSticker}')
  paths.append('/members/{idMember}/savedSearches/{idSavedSearch}')
  paths.append('/notifications/{idNotification}')
  paths.append('/notifications/{idNotification}/unread')
  paths.append('/notifications/all/read')
  paths.append('/organizations/{idOrg}')
  paths.append('/organizations/{idOrg}/desc')
  paths.append('/organizations/{idOrg}/displayName')
  paths.append('/organizations/{idOrg}/members')
  paths.append('/organizations/{idOrg}/members/{idMember}')
  paths.append('/organizations/{idOrg}/members/{idMember}/deactivated')
  paths.append('/organizations/{idOrg}/memberships/{idMembership}')
  paths.append('/organizations/{idOrg}/name')
  paths.append('/organizations/{idOrg}/prefs/associatedDomain')
  paths.append('/organizations/{idOrg}/prefs/boardVisibilityRestrict/org')
  paths.append('/organizations/{idOrg}/prefs/boardVisibilityRestrict/private')
  paths.append('/organizations/{idOrg}/prefs/boardVisibilityRestrict/public')
  paths.append('/organizations/{idOrg}/prefs/externalMembersDisabled')
  paths.append('/organizations/{idOrg}/prefs/googleAppsVersion')
  paths.append('/organizations/{idOrg}/prefs/orgInviteRestrict')
  paths.append('/organizations/{idOrg}/prefs/permissionLevel')
  paths.append('/organizations/{idOrg}/website')
  paths.append('/organizations')
  paths.append('/organizations/{idOrg}/logo')
  paths.append('/organizations/{idOrg}')
  paths.append('/organizations/{idOrg}/logo')
  paths.append('/organizations/{idOrg}/members/{idMember}')
  paths.append('/organizations/{idOrg}/members/{idMember}/all')
  paths.append('/organizations/{idOrg}/prefs/associatedDomain')
  paths.append('/organizations/{idOrg}/prefs/orgInviteRestrict')
  paths.append('/sessions/{idSession}')
  paths.append('/sessions/{idSession}/status')
  paths.append('/sessions')
  paths.append('/tokens/{token}/webhooks')
  paths.append('/tokens/{token}/webhooks')
  paths.append('/tokens/{token}')
  paths.append('/tokens/{token}/webhooks/{idWebhook}')
  paths.append('/webhooks/{idWebhook}')
  paths.append('/webhooks/')
  paths.append('/webhooks/{idWebhook}/active')
  paths.append('/webhooks/{idWebhook}/callbackURL')
  paths.append('/webhooks/{idWebhook}/description')
  paths.append('/webhooks/{idWebhook}/idModel')
  paths.append('/webhooks')
  paths.append('/webhooks/{idWebhook}')

  pat = re.compile('^/[a-zA-Z]+/[a-zA-Z]+/[a-zA-Z]+$')

  # cnt = 1
  # for pattern in PATH_PATTERNS :
  #   idx = 0
  #   for path in paths :
  #     mm = pattern.match(path)
  #     if mm :
  #       print(">>~~~~~ {} -- {}   {} ~~~~<<".format(cnt, idx, path))
  #       # if cnt == 8 : print(">> ,\"{}\" <<".format(path.split('/')[1]))
  #       # if cnt == 8 : print(">> ,\"{}\" <<".format(pat.match(path).group(0)))
  #     idx = idx+1
  #   cnt = cnt+1

  cnt = 1
  tot = 0
  for path in paths :
    idx = 0
    for pattern in PATH_PATTERNS :
      mm = pattern.match(path)
      if mm :
        tot = tot+1
        print(">>~~~~~ {}/{} -- {}   {} ~~~~<<".format(cnt, tot, idx, path))
      idx = idx+1
    cnt = cnt+1

  print("\n>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<\n")



if __name__ == "__main__": main()

