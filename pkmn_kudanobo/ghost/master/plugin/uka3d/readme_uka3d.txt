========================================================================
【ソフト名称】Uka3D β 0.3.0.0
【 制 作 者 】yasi
【 動作環境 】WindowsXP SP3 DirectX9.0C以降
【 タ イ プ 】「伺か(SSP専用)」3D描画SAORIモジュール
【 取扱種別 】フリーウェア
【 配布月日 】2021/06/22
【 配 布 元 】http://seesaawiki.jp/uka3d/
【  備  考  】後述
========================================================================
■概要

  デスクトップマスコットアプリケーション「伺か(SSP専用)」3D描画SAORIモジュールの
  βテスト版です。
  「伺か」に3D描画機能を搭載する事で3Dデスクトップマスコットの作成を安易にする事を
  目的とし、開発を進めています。

  デスクトップマスコットアプリケーション「伺か」について詳しくはこちらをご覧ください。
  ばぐとら研究所
    http://ssp.shillest.net/


■使用方法

  ダウンロードしたzipファイルを書込み可能な任意のフォルダへ解凍後、使用するSHIORIの
  仕様手順に従ってuka3d_proxy.dll、uka3d.exe、本readme_uka3d.txtを配置・使用して下さい。
  
  Uka3D詳しい使用方法・規格は公式サイトhttp://seesaawiki.jp/uka3d/をご覧ください。


■注意事項

  本SAORIは開発途中の物であり、告知なく仕様等が変更される恐れがあります。予めご了承ください。


■キーボード操作

　デフォルトではOFFになっていますが、ゴデベが任意にRequestを送る事で、
  キーボード操作をON/OFFにする事が可能です。

○Dキー/インフォメーションモード切替
  各種情報の描画モードを切替ます。
  基本的に作者のデバッグ用の物です。

　【デバッグ情報表示】
  ・モード1
   FPS値を表示します。
   （以下のモード全てでFPS値は描画されます。）

  ･モード2
   ワールド座標原点を基準とした三次元軸を描画します。
   （以下のモード全てで三次元軸は描画されます）

  ･モード3
   カメラの各種パラメータを描画します。
   Nearは描画可能最小距離、Farは描画可能最大距離。
   Posはワールド座標カメラ位置。
   Lengthは注視点とのカメラ距離
   Angle of Viewは垂直画角。
   AHは注視点正面位置を0°としたカメラの水平角度、AVは垂直角度を表します。

  ･モード4
   ライトの各種パラメータを描画します。
   キーライトにはディレクショナルライト（非減衰平行光源）が設定されています。
   DifCはキーライトのディフューズカラー（拡散光）のRGB値。
   SpcCはキーライトのスペキュラーカラー（反射光）のRGB値。
   AmbCはキーライトのアンビエントカラー（環境光）のRGB値。
   Posはキーライトの位置。
   Dirはキーライトが向いている方向（正規化ベクトル）。
   Ang Hは水平角度、Vは垂直角度。
   GAmbCはグローバルアンビエントカラー（大域環境光）のRGB値を表します。


  ･モード5
   マウスの各種パラメータを描画します。
   Posはウィンドウ内のマウスポインタ座標。
   ModelHは当り判定をしたモデルハンドル。
   Materialは当ったマテリアルNo'。
   PlayIDは再生中モーションID。
   Rateはモーションブレンド率


○カメラ･ライト操作
  ※カメラ操作モードとライト操作モードは同時にONにはできません。
  　一方がON時にもう一方をONにすると先にONになっていた方は自動的にOFFになります。
    ゴースト辞書内でフラグを管理する場合はこれを踏まえて注意してください。

  【カメラモード】
    ･↑↓←→キー/カメラ回転
     注視点を中心にカメラを回転させます。
     左右には360°回転しますが、上下は一定値で止まります。

    ･Alt+↑↓キー/注視点&視点（カメラ）の高さ変更
     注視点と視点の高さを一緒に変更します。

    ･Alt+←→キー/カメラ距離変更
     カメラの注視点からの距離（ドリー）を変更します。
   

    ･Ctrl+↑↓キー/Far値変更
     描画可能最大距離を変更します。
     Near値以下に変更する事はできません。

    ･Ctrl+←→キー/Near値変更
     描画可能最小距離を変更します。
     Far値以上に変更する事はできません。

    ･Shift+↑↓キー/Angle of View値変更
     垂直画角（ズーム）を変更します。
     値が小さくなるほど望遠に、大きくなるほど広角になります。
     広角になるほどパースが強くなります。

  【ライトモード】
    ･↑↓←→キー/キーライト回転
     ライトの照射方向を変更します。

    ･Ctrl+↑↓キー/アンビエントカラーR値変更
     キーライトの環境光R値を変更します。

    ･Alt+↑↓キー/アンビエントカラーG値変更
     キーライトの環境光G値を変更します。

    ･Shift+↑↓キー/アンビエントカラーB値変更
     キーライトの環境光B値を変更します。

    

■免責事項

  本ソフトウェアとはメインプログラムであるuka3d_proxy.dll及びuka3d.exeの事を示します。
  本ソフトウェア及び、同梱の各種ファイルを使用した事によって発生する
  いかなる不具合に対しても本ソフトウェア作者は一切の責任を負いません。
  自己責任にて使用願います。
  又、予告無く開発及び配布を中止する場合があります。
  あらためてご了承願います。


■謝辞及びライセンス

  本ソフトウェアの開発には、DXライブラリを使用させていただいてます。
  またSAORI化にはCSAORIを使用させていただいてます。

  本ソフトウェアの著作権はyasiに帰属します。
  伺かに関する利用の場合、当テキストを添付していただければ
  同梱・再配布は自由に行って頂いて構いません。
  
  それら以外の利用については事前に下記連絡先へ連絡していただくようお願いします。
  

 ○DXライブラリ機能に関わる著作権表示

　　　libjpeg　Copyright (C) 1991-2013, Thomas G. Lane, Guido Vollbeding.
　　　this software is based in part on the work of the Independent JPEG Group


　　　libpng　Copyright (C) 2004, 2006-2012 Glenn Randers-Pehrson.
　　　zlib　Copyright (C) 1995-2012 Jean-loup Gailly and Mark Adler.


　　　libtiff　Copyright (c) 1988-1997 Sam Leffler
　　　libtiff　Copyright (c) 1991-1997 Silicon Graphics, Inc.

　　　Permission to use, copy, modify, distribute, and sell this software and
　　　its documentation for any purpose is hereby granted without fee, provided
　　　that (i) the above copyright notices and this permission notice appear in
　　　all copies of the software and related documentation, and (ii) the names of
　　　Sam Leffler and Silicon Graphics may not be used in any advertising or
　　　publicity relating to the software without the specific, prior written
　　　permission of Sam Leffler and Silicon Graphics.

　　　THE SOFTWARE IS PROVIDED "AS-IS" AND WITHOUT WARRANTY OF ANY KIND,
　　　EXPRESS, IMPLIED OR OTHERWISE, INCLUDING WITHOUT LIMITATION, ANY
　　　WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

　　　IN NO EVENT SHALL SAM LEFFLER OR SILICON GRAPHICS BE LIABLE FOR
　　　ANY SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY KIND,
　　　OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
　　　WHETHER OR NOT ADVISED OF THE POSSIBILITY OF DAMAGE, AND ON ANY THEORY OF
　　　LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
　　　OF THIS SOFTWARE.


　　　libogg　Copyright (C) 2002-2009 Xiph.org Foundation

　　　Redistribution and use in source and binary forms, with or without
　　　modification, are permitted provided that the following conditions
　　　are met:

　　　- Redistributions of source code must retain the above copyright
　　　notice, this list of conditions and the following disclaimer.

　　　- Redistributions in binary form must reproduce the above copyright
　　　notice, this list of conditions and the following disclaimer in the
　　　documentation and/or other materials provided with the distribution.

　　　- Neither the name of the Xiph.org Foundation nor the names of its
　　　contributors may be used to endorse or promote products derived from
　　　this software without specific prior written permission.

　　　THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
　　　``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
　　　LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
　　　A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE FOUNDATION
　　　OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
　　　SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
　　　LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
　　　DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
　　　THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
　　　(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
　　　OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


　　　Opus audio codec
　　　Copyright 2001-2011 Xiph.Org, Skype Limited, Octasic,
　　　 Jean-Marc Valin, Timothy B. Terriberry,
　　　 CSIRO, Gregory Maxwell, Mark Borgerding,
　　　 Erik de Castro Lopo

　　　Redistribution and use in source and binary forms, with or without
　　　modification, are permitted provided that the following conditions
　　　are met:

　　　- Redistributions of source code must retain the above copyright
　　　notice, this list of conditions and the following disclaimer.

　　　- Redistributions in binary form must reproduce the above copyright
　　　notice, this list of conditions and the following disclaimer in the
　　　documentation and/or other materials provided with the distribution.

　　　- Neither the name of Internet Society, IETF or IETF Trust, nor the
　　　names of specific contributors, may be used to endorse or promote
　　　products derived from this software without specific prior written
　　　permission.

　　　THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
　　　``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
　　　LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
　　　A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
　　　OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
　　　EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
　　　PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
　　　PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
　　　LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
　　　NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
　　　SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


　　　Opusfile
　　　Copyright (c) 1994-2013 Xiph.Org Foundation and contributors

　　　Redistribution and use in source and binary forms, with or without
　　　modification, are permitted provided that the following conditions
　　　are met:

　　　- Redistributions of source code must retain the above copyright
　　　notice, this list of conditions and the following disclaimer.

　　　- Redistributions in binary form must reproduce the above copyright
　　　notice, this list of conditions and the following disclaimer in the
　　　documentation and/or other materials provided with the distribution.

　　　- Neither the name of the Xiph.Org Foundation nor the names of its
　　　contributors may be used to endorse or promote products derived from
　　　this software without specific prior written permission.

　　　THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
　　　``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
　　　LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
　　　A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE FOUNDATION
　　　OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
　　　SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
　　　LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
　　　DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
　　　THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
　　　(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
　　　OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


　　　Mersenne Twister
　　　Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
　　　All rights reserved.

　　　Redistribution and use in source and binary forms, with or without
　　　modification, are permitted provided that the following conditions
　　　are met:

　　　1. Redistributions of source code must retain the above copyright
　　　notice, this list of conditions and the following disclaimer.

　　　2. Redistributions in binary form must reproduce the above copyright
　　　notice, this list of conditions and the following disclaimer in the
　　　documentation and/or other materials provided with the distribution.

　　　3. The name of the author may not be used to endorse or promote products
　　　derived from this software without specific prior written permission.

　　　THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
　　　IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
　　　OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
　　　IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
　　　INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
　　　NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
　　　DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
　　　THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
　　　(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
　　　THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


　　　Bullet　Copyright (c) 2003-2006 Erwin Coumans.
    

　　　DX Library Copyright (C) 2001-2021 Takumi Yamada.


■連絡先

  本ソフトフェアご使用にあたり、感想・ご要望・バグなどありましたらこちらまでお願いします。
  今後のモジュール開発の参考とさせていただきます。

  mail    : home@mydimension.jp
  url     : http://www.mydimension.jp
  twitter : http://twitter.com/yasi_naga