from qtsymbols import *
import functools
from myutils.config import globalconfig, magpie_config, static_data, _TRL
from gui.inputdialog import getsomepath1
from gui.usefulwidget import (
    D_getsimplecombobox,
    makegrid,
    D_getspinbox,
    getvboxwidget,
    D_getIconButton,
    makesubtab_lazy,
    makescrollgrid,
    D_getsimpleswitch,
)


def makescalew(self, lay):

    commonfsgrid = [
        [
            ("缩放方式", 4),
            (
                D_getsimplecombobox(
                    static_data["scalemethods_vis"],
                    globalconfig,
                    "fullscreenmethod_4",
                ),
                6,
            ),
        ]
    ]

    losslessgrid = [
        [
            ("Magpie_路径", 4),
            (
                D_getIconButton(
                    callback=lambda : getsomepath1(
                        self,
                        "Magpie_路径",
                        globalconfig,
                        "magpiepath",
                        "Magpie_路径",
                        isdir=True,
                    ),
                    icon="fa.gear",
                ),
                1,
            ),
            ("", 10),
        ]
    ]

    innermagpie = [
        [
            (
                dict(
                    title="常规",
                    grid=(
                        [
                            [
                                "缩放模式",
                                D_getsimplecombobox(
                                    [_["name"] for _ in magpie_config["scalingModes"]],
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "scalingMode",
                                ),
                            ],
                            [
                                "捕获模式",
                                D_getsimplecombobox(
                                    [
                                        "Graphics Capture",
                                        "Desktop Duplication",
                                        "GDI",
                                        "DwmSharedSurface",
                                    ],
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "captureMethod",
                                ),
                            ],
                            [
                                "3D游戏模式",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "3DGameMode",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
        [
            (
                dict(
                    title="性能",
                    grid=(
                        [
                            [
                                "显示帧率",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "showFPS",
                                ),
                            ],
                            [
                                "限制帧率",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "frameRateLimiterEnabled",
                                ),
                            ],
                            [
                                "最大帧率",
                                D_getspinbox(
                                    0,
                                    9999,
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "maxFrameRate",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
        [
            (
                dict(
                    title="源窗口",
                    grid=(
                        [
                            [
                                "缩放时禁用窗口大小调整",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "disableWindowResizing",
                                ),
                            ],
                            [
                                "捕获标题栏",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "captureTitleBar",
                                ),
                            ],
                            [
                                "自定义剪裁",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "croppingEnabled",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
        [
            (
                dict(
                    title="光标",
                    grid=(
                        [
                            [
                                "绘制光标",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "drawCursor",
                                ),
                            ],
                            [
                                "绘制光标_缩放系数",
                                D_getsimplecombobox(
                                    [
                                        "0.5x",
                                        "0.75x",
                                        "无缩放",
                                        "1.25x",
                                        "1.5x",
                                        "2x",
                                        "和源窗口相同",
                                    ],
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "cursorScaling",
                                ),
                            ],
                            [
                                "绘制光标_插值算法",
                                D_getsimplecombobox(
                                    ["最邻近", "双线性"],
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "cursorInterpolationMode",
                                ),
                            ],
                            [
                                "缩放时调整光标速度",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "adjustCursorSpeed",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
        [
            (
                dict(
                    title="高级",
                    grid=(
                        [
                            [
                                "禁用DirectFlip",
                                D_getsimpleswitch(
                                    magpie_config["profiles"][
                                        globalconfig["profiles_index"]
                                    ],
                                    "disableDirectFlip",
                                ),
                            ],
                            [
                                "允许缩放最大化或全屏的窗口",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "allowScalingMaximized",
                                ),
                            ],
                            [
                                "缩放时模拟独占全屏",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "simulateExclusiveFullscreen",
                                ),
                            ],
                            [
                                "内联效果参数",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "inlineParams",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
        [
            (
                dict(
                    title="开发者选项",
                    grid=(
                        [
                            [
                                "调试模式",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "debugMode",
                                ),
                            ],
                            [
                                "禁用效果缓存",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "disableEffectCache",
                                ),
                            ],
                            [
                                "禁用字体缓存",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "disableFontCache",
                                ),
                            ],
                            [
                                "解析效果时保存源代码",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "saveEffectSources",
                                ),
                            ],
                            [
                                "编译效果时将警告视为错误",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "warningsAreErrors",
                                ),
                            ],
                            [
                                "检测重复帧",
                                D_getsimplecombobox(
                                    ["总是检测", "动态检测", "从不检测"],
                                    magpie_config,
                                    "duplicateFrameDetectionMode",
                                ),
                            ],
                            [
                                "启用动态检测统计",
                                D_getsimpleswitch(
                                    magpie_config,
                                    "enableStatisticsForDynamicDetection",
                                ),
                            ],
                        ]
                    ),
                ),
                0,
                "group",
            )
        ],
    ]

    vw, vl = getvboxwidget()
    lay.addWidget(vw)
    gw, gd = makegrid(commonfsgrid, delay=True)
    vl.addWidget(gw)
    tw, td = makesubtab_lazy(
        _TRL(["Magpie", "外部缩放软件"]),
        [
            functools.partial(makescrollgrid, innermagpie),
            functools.partial(makescrollgrid, losslessgrid),
        ],
        delay=True,
    )
    vl.addWidget(tw)
    gd()
    td()
