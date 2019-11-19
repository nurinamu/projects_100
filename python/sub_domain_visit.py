from typing import List

class DomainNode:
    def __init__(self) :
        self.val = 0
        self.sub = {}

class Solution:
    
    
    def buildNode(self, domains:str, rootDomain:DomainNode) :
        splited = domains.split(' ')
        subs = splited[1].split('.')
        parent = rootDomain
        for idx in range(len(subs)-1, -1, -1) :
            if subs[idx] not in parent.sub :
                parent.sub[subs[idx]] = DomainNode()
            parent = parent.sub[subs[idx]]
        parent.val += int(splited[0])
        
    def printDomains(self, domains:DomainNode, domainName:str, result:List[str]) -> int :
        point = 0
        for subDomain in domains.sub :
            if domainName != "" :
                point += self.printDomains(domains.sub[subDomain], "{}.{}".format(subDomain, domainName), result)
            else :
                point += self.printDomains(domains.sub[subDomain], subDomain, result)
        if domainName != "" :
            result.append("{} {}".format(domains.val + point, domainName) )
        return domains.val + point
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = DomainNode()
        result = []

        for domain in cpdomains :
            self.buildNode(domain, domains)

        self.printDomains(domains, "", result)

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subdomainVisits(["9656 hoh.ca","1311 sci.net","1945 jre.us","9323 kvk.com","8682 whf.unn.com","9895 xow.fsw.us","6881 epf.gdw.net","7566 gjf.network","1216 kwd.network","5262 iux.net","3377 pjp.qzi.org","9460 ato.co","2735 ibf.co","3953 jfz.team","4543 bkn.ajl.net","9699 gtu.us","3923 wwo.zqy.org","9495 wph.org","8000 hpn.org","7632 roc.hlr.com","8531 xuf.jkx.ca","9251 miu.kmz.team","1050 uyf.gxz.org","5726 xuf.network","720 pgl.hlr.us","4979 wqv.com","2055 nkh.uyy.com","1463 xhe.ca","9761 fsw.team","2750 arz.org","8188 dfa.com","5263 rbg.network","5045 unn.network","7261 ara.org","8650 azh.jre.team","9906 xpn.ajl.team","7060 lmx.czb.org","1495 epf.co","7717 qhr.okv.ca","866 sur.tjy.ca","2550 zfr.epf.co","1358 gbq.ca","2470 gjf.ca","7125 btv.com","3809 kmx.network","1551 shc.buf.ca","6066 qeu.gqs.co","5389 fhm.epf.org","8131 qay.us","4118 bva.rbg.co","1947 ato.com","8801 ara.us","9171 hal.team","2377 jqz.mkw.org","2222 plj.ytn.co","9096 ser.org","1 zhy.net","6385 tzz.fzx.co","9553 iux.org","9572 zqy.com","7131 ojr.net","2393 upo.ibf.co","8236 nxm.ixi.com","272 nei.hpn.org","5036 qxw.kmx.ca","8918 kmx.team","7025 hkt.ca","5981 tad.lfn.com","6293 jia.net","8327 vfo.hnl.us","4169 lkl.cwn.com","8107 hkt.network","6632 hax.wip.net","3672 hwu.com","8459 vjx.uyy.network","3012 gjf.net","4036 ksc.ca","7746 yls.org","8694 asz.org","4439 htq.com","4582 xuf.org","2205 wrw.srp.ca","9479 iun.hlr.co","6752 kov.ato.us","7504 qzk.rbg.net","9715 ajl.network","4008 cke.fqv.com","2612 tvj.kmz.org","8966 zfz.org","5407 qhk.bfo.net","9019 hal.team","3576 avm.ajl.ca","4544 vec.amr.team","9679 umx.dfa.ca","2223 lux.zqk.team","5004 syf.vbo.us","1998 ltq.org","1895 xvi.ajl.network","9548 unn.us","1558 okv.network"]))

