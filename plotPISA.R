data <- list()
for (i in 0:10) {
    file <- sprintf("p%d.xml.out",i)
    data[[i+1]] <- read.table(file,header=F)
}
chains=c("A","B")
for (chain in chains) {
    plotfile=sprintf("plot%s.tiff",chain)
    tiff(plotfile,res=300,width=4,height=4,units='in')
    for (i in 1:11) {
        bsa.in <- data[[i]]
        bsa.chain <- bsa.in[bsa.in$V3==chain,]
        bsa <- bsa.chain$V5/bsa.chain$V4
        if (i==1) {
            plot(bsa,type="l",col=1)
        }
        lines(bsa,col=i)
    }
    dev.off()
}

