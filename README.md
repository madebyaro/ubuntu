
# imaging

Make an image of a digital ocean droplet  

ssh root@x.y.z.196 "dd if=/dev/vda1 | gzip -1 -" | dd of=image.196.gz


