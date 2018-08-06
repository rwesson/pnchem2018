#!#!/usr/bin/Rscript

d1<-scan("adfs_all_log")
d2<-scan("adfs_hdef_log")
d3<-scan("adfs_b_log")
d4<-scan("adfs_hdef_nowels_log")
d5<-scan("adfs_nohdef_log")
d6<-scan("adfs_nob_log")

h<-scan("adfs_hii")
h1<-scale(h)

p<-scan("adfs_pne")
p1<-scale(p)

ytitle <- expression(paste(italic("adf"), " (hydrogen-deficient central stars)"))


png("qqplot1.png")
qqplot(d1,d2,xlab=expression(paste(italic("adf"),"(all nebulae)")),ylab=ytitle,xlim=c(-0.5,3.0),ylim=c(-0.5,3.0))
segments(-0.5,-0.5,3,3,lty=2)
dev.off()

png("qqplot2.png")
qqplot(d1,d4,xlab=expression(paste(italic("adf"),"(all nebulae)")),ylab=expression(paste(italic("adf"),"(hydrogen-deficient central stars excluding WELs)")),xlim=c(-0.5,3.0),ylim=c(-0.5,3.0))
segments(-0.5,-0.5,3,3,lty=2)
dev.off()

png("qqplot3.png")
qqplot(d1,d3,xlab=expression(paste(italic("adf"),"(all nebulae)")),ylab=expression(paste(italic("adf"),"(known close binaries)")),xlim=c(-0.5,3.0),ylim=c(-0.5,3.0))
segments(-0.5,-0.5,3,3,lty=2)
dev.off()

png("qqplot4.png")
qqplot(d5,d2,xlab=expression(paste(italic("adf"),"(central stars not classified as H-deficient)")),ylab=expression(paste(italic("adf"),"(hydrogen-deficient central stars excluding WELs)")),xlim=c(-0.5,3.0),ylim=c(-0.5,3.0))
segments(-0.5,-0.5,3,3,lty=2)
dev.off()

png("qqplot5.png")
qqplot(d6,d3,xlab=expression(paste(italic("adf"),"(central stars not known to be binary)")),ylab=expression(paste(italic("adf"),"(known close binaries)")),xlim=c(-0.5,3.0),ylim=c(-0.5,3.0))
segments(-0.5,-0.5,3,3,lty=2)
dev.off()

png("qqplot_hii.png")
qqnorm(h1,xlim=c(-3.0,3.0),ylim=c(-3.0,3.0))
segments(-3,-3,3,3,lty=2)
dev.off()

png("qqplot_pne.png")
qqnorm(p1,xlim=c(-3.0,3.0),ylim=c(-3.0,3.0))
segments(-3,-3,3,3,lty=2)
dev.off()
