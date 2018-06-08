class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        m={}
        for d in cpdomains:
            d = d.split()
            c = int(d[0])
            d='.'+ d[1]
            for i in range(len(d)):
                if i ==0 or d[i]==".":
                    if d[i+1:] in m:
                        m[d[i+1:]]+=c
                    else:
                        m[d[i+1:]]=c
        ret=[]
        for e in m:
            ret.append(str(m[e])+ ' ' + e)
        return ret

print Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])

