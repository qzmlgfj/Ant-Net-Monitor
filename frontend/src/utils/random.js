let base = new Date().getTime()
const onesecond = 1000

/**
 * 产生一对包含时间戳的随机数
 */
const random = () => {
    const timestamp = new Date(base += onesecond)
    const random = Math.random().toFixed(2)
    return [timestamp, random]
}

/**
 * 产生一个随机数组
 */
const randomArray = () => {
    const array = []
    for (let i = 0; i < 100; i++) {
        array.push(random())
    }
    return array
}
