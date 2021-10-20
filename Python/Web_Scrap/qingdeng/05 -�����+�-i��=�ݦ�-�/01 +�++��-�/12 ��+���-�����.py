
html = """
<script type="text/javascript">
    var fp = new FlexPaperViewer(
        'http://bulletin.sntba.com/FlexPaperViewer',
        'viewerPlaceHolder', {
            config : {
                SwfFile : escape('http://bulletin.sntba.com/project//2020-01/noticeFile/Z6101002181N01555001/8aa946a756a24b09aded43c7bdd5f348.swf'),
                EncodeURI : true,
                Scale : 0.6,
                ZoomTransition : 'easeOut',
                ZoomTime : 0.5,
                ZoomInterval : 0.05,
                FitPageOnLoad : true,
                FitWidthOnLoad : true,
                PrintEnabled: false,//是否支持打印
                FullScreenAsMaxWindow : false,
                ProgressiveLoading : true,
                MinZoomSize : 0.05,
                MaxZoomSize : 5,
                SearchMatchAll : false,
                InitViewMode : 'Portrait',
                ViewModeToolsVisible : true,
                ZoomToolsVisible : true,
                NavToolsVisible : true,
                CursorToolsVisible : true,
                SearchToolsVisible : false,
                localeChain : 'zh_CN'
            }
        });
</script>
"""

import re


# 学习的正则的所有元字符\t  \\ \n \t ...  如果出现在需要匹配的字符串中, 那么需要转义, 转义就把具有特殊含义的字符当做普通字符串处理
result = re.findall("SwfFile : escape\('(.*?)'\),", html, re.S)
print(result)

