module.exports = {
    outputDir: '../ant_net_monitor/dist',
    assetsDir: 'static',
    indexPath: 'index.html',
    devServer: {
        proxy: 'http://localhost:5000'
    },
}