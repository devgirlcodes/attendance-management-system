def egcd(a, b):
    if a==0:
        return(b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return(g, x-(b//a)*y,y)

def modinv(a, m):
    g, x, y = egcd(a,m)
    if g!=1:
        raise Exception('modular inverse does not exist')
    else:
        return x%m

c = 385287122231303418995932004995458476137044889050263274490592257240071088642641590238881343760363122835968400100731425741775337575700046776670663987541025717947884411805114531064129058438076401337559203921529647739237
n = 21240130069302595435883573568292543584653982426668643904196630885984119007899960150162877143271928662185885422702123670222165981446412189843665571992895649937195036232374014356896167929469467494531756153911013832353810970941919101050971790197002016280790620714887304192321101311465703150098410331176735899796484284165771555960758054286754565310439163189954842301676099617954811528874343372426916478057819577132937062857039063351856289801979923260408285890418889829381378968646646737194160697920287161229178345666260994127087040393511692642122516019055570881253021165130706539874713965212158253699181636631222365809257
e = 3

p = 21240130069302595435883573568292543584653982426668643904196630885984119007899960150162877143271928662185885422702123670222165981446412189843665571992895649937195036232374014356896167929469467494531756153911013832353810970941919101050971790197002016280790620714887304192321101311465703150098410331176735899796484284165771555960758054286754565310439163189954842301676099617954811528874343372426916478057819577132937062857039063351856289801979923260408285890418889829381378968646646737194160697920287161229178345666260994127087040393511692642122516019055570881253021165130706539874713965212158253699181636631222365809257
q = 21240130069302595435883573568292543584653982426668643904196630885984119007899960150162877143271928662185885422702123670222165981446412189843665571992895649937195036232374014356896167929469467494531756153911013832353810970941919101050971790197002016280790620714887304192321101311465703150098410331176735899796484284165771555960758054286754565310439163189954842301676099617954811528874343372426916478057819577132937062857039063351856289801979923260408285890418889829381378968646646737194160697920287161229178345666260994127087040393511692642122516019055570881253021165130706539874713965212158253699181636631222365809257

phi = (p-1)*(q-1)
d = modinv(e,phi)

m = pow(c, d, n)

print(m)
print(hex(m))
print(bytes.fromhex(hex(m)[2:]).decode('ascii'))
