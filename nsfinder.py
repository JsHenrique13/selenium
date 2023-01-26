"""import dns.resolver


arquivo = 'lista.txt'
ns = list()

with open(arquivo, 'r') as lista:
    for host in lista:
        print(host)
        my_resolver = dns.resolver.Resolver()
        result = my_resolver.resolve(host, 'NS')
        for val in result:
                print('NS Record : ', val.to_text())
         
"""
import dns.resolver

arquivo = 'lista.txt'
ns = list()
with open(arquivo, 'r') as lista:
    for host in lista:
        my_resolver = dns.resolver.Resolver()
        try:
            result = my_resolver.resolve(host[0:-1], 'NS')
            for val in result:
                ns.append(val.to_text())
            # print(host[0:-1], ns, )
            
        except:
            pass
        try:
            result = my_resolver.resolve(host[0:-1], 'A')
            for val in result:    
                print(host[0:-1], val.to_text(), ns)
                ns.clear()
        except:
            pass

