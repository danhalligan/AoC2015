dat = IO.read("input.txt");
dat.scan(/\(/).length - dat.scan(/\)/).length

dat = dat.split('').map {|i| i == '(' ? 1 : -1}
i = 0
sum = 0
while sum != -1
  sum += dat[i]
  i += 1
end
