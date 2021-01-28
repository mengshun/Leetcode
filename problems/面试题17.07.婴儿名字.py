"""
面试题 17.07. 婴儿名字
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择 字典序最小 的名字作为真实名字。

 

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
"""

import collections
class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            x, y = y, x

        self.father[x] = y
        self.size[y] += self.size[x]


def trulyMostPopular(names, synonyms):

    # 将数量解析至每一个名字下面
    name_count = collections.defaultdict(int)
    # 每个名字对应唯一序号
    name_index = {}
    # 名字列表
    name_list = set()
    for v in names:
        res = v.split(")")[0].split("(")
        if len(res) == 2:
            name, count = res
            name_count[name] = int(count)
            name_index[name] = len(name_index)
            name_list.add(name)

    # names 名字列表可能不全, 需要把 关系表里的名字在排查一遍
    # 格式化名字
    formatter_synonyms = []
    for v in synonyms:
        res = v[1:-1].split(",")
        formatter_synonyms.append(res)
        n1, n2 = res
        if n1 not in name_index:
            name_index[n1] = len(name_index)
            name_list.add(n1)
        if n2 not in name_index:
            name_index[n2] = len(name_index)
            name_list.add(n2)

    # 创建并查集
    uf = UnionFind(len(name_index))

    #开始连线
    for x, y in formatter_synonyms:
        if x in name_index and y in name_index:
            uf.merge(name_index[x], name_index[y])

    #进行分组
    group = collections.defaultdict(list)
    for name in name_list:
        group[uf.find(name_index[name])].append(name)

    #对同一组的名下的数量进行累加
    res = []
    for vl in group.values():
        min_name = min(vl)
        res_count = 0
        for name in vl:
            res_count += name_count[name]
        res.append("{}({})".format(min_name, res_count))
    return res





print(trulyMostPopular(["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]))


counts = ["Fcclu(70)","Ommjh(63)","Dnsay(60)","Qbmk(45)","Unsb(26)","Gauuk(75)","Wzyyim(34)","Bnea(55)","Kri(71)","Qnaakk(76)","Gnplfi(68)","Hfp(97)","Qoi(70)","Ijveol(46)","Iidh(64)","Qiy(26)","Mcnef(59)","Hvueqc(91)","Obcbxb(54)","Dhe(79)","Jfq(26)","Uwjsu(41)","Wfmspz(39)","Ebov(96)","Ofl(72)","Uvkdpn(71)","Avcp(41)","Msyr(9)","Pgfpma(95)","Vbp(89)","Koaak(53)","Qyqifg(85)","Dwayf(97)","Oltadg(95)","Mwwvj(70)","Uxf(74)","Qvjp(6)","Grqrg(81)","Naf(3)","Xjjol(62)","Ibink(32)","Qxabri(41)","Ucqh(51)","Mtz(72)","Aeax(82)","Kxutz(5)","Qweye(15)","Ard(82)","Chycnm(4)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Lucf(62)","Uhsg(23)","Csh(39)","Txixz(87)","Kgabb(80)","Weusps(79)","Nuq(61)","Drzsnw(87)","Xxmsn(98)","Onnev(77)","Owh(64)","Fpaf(46)","Hvia(6)","Kufa(95)","Chhmx(66)","Avmzs(39)","Okwuq(96)","Hrschk(30)","Ffwni(67)","Wpagta(25)","Npilye(14)","Axwtno(57)","Qxkjt(31)","Dwifi(51)","Kasgmw(95)","Vgxj(11)","Nsgbth(26)","Nzaz(51)","Owk(87)","Yjc(94)","Hljt(21)","Jvqg(47)","Alrksy(69)","Tlv(95)","Acohsf(86)","Qejo(60)","Gbclj(20)","Nekuam(17)","Meutux(64)","Tuvzkd(85)","Fvkhz(98)","Rngl(12)","Gbkq(77)","Uzgx(65)","Ghc(15)","Qsc(48)","Siv(47)"]
names = ["(Gnplfi,Qxabri)","(Uzgx,Siv)","(Bnea,Lucf)","(Qnaakk,Msyr)","(Grqrg,Gbclj)","(Uhsg,Qejo)","(Csh,Wpagta)","(Xjjol,Lucf)","(Qoi,Obcbxb)","(Npilye,Vgxj)","(Aeax,Ghc)","(Txixz,Ffwni)","(Qweye,Qsc)","(Kri,Tuvzkd)","(Ommjh,Vbp)","(Pgfpma,Xxmsn)","(Uhsg,Csh)","(Qvjp,Kxutz)","(Qxkjt,Tlv)","(Wfmspz,Owk)","(Dwayf,Chycnm)","(Iidh,Qvjp)","(Dnsay,Rngl)","(Qweye,Tlv)","(Wzyyim,Kxutz)","(Hvueqc,Qejo)","(Tlv,Ghc)","(Hvia,Fvkhz)","(Msyr,Owk)","(Hrschk,Hljt)","(Owh,Gbclj)","(Dwifi,Uzgx)","(Iidh,Fpaf)","(Iidh,Meutux)","(Txixz,Ghc)","(Gbclj,Qsc)","(Kgabb,Tuvzkd)","(Uwjsu,Grqrg)","(Vbp,Dwayf)","(Xxmsn,Chhmx)","(Uxf,Uzgx)"]
print(trulyMostPopular(counts, names))

print(trulyMostPopular(["a(10)","c(13)"], ["(a,b)","(c,d)","(b,c)"]))
