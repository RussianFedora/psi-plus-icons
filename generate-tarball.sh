#! /bin/sh

rm -fr resources
git clone git://github.com/psi-plus/resources.git
rev=$(cd resources && git log -1 --pretty=%h iconsets)
pkgrev=$(date +%Y%m%d)git${rev}
psiver=0.16-${pkgrev}
# remove non-free kolobok smiles
rm -f resources/iconsets/emoticons/kolobok*.jisp
tar -C resources/ -czf psi-plus-icons-${psiver}.tar.gz iconsets

