import { ref } from "vue";

/**
 * ECharts需要的数据格式
 */
let series = [];
/**
 * 作为名称映射，用于将后端传回数据字段的名称转换为变量名
 */
let seriesDict = {};

/**
 * 
 * @param {string} name 
 * @returns {Object} 单个Series条目
 */
function initSingleObject(name) {
    return {
        name: name,
        type: "line",
        smooth: false,
        symbol: "none",
        areaStyle: {},
        data: ref([]),
    };
}

/**
 * 初始化Series，不包含具体数据
 * @param {Object} data，单条数据，用于解析并生成对应的条目
 */
function initSeries(data) {
    series = [];
    seriesDict = {};

    for (const name of Object.keys(data)) {
        if (name === "time_stamp" || name === "id") {
            continue;
        }
        let singleObject = initSingleObject(name);
        series.push(singleObject);
        seriesDict[name] = singleObject;
    }
}

/**
 * 装填数据
 * @param {Object} data 完整的数据
 * @returns {Object} 完整的Series
 */
function setSeries(data) {
    const clearSeries = () => {
        series.forEach(item => {
            item.data.value = [];
        });
    }

    clearSeries();

    data.forEach(item => {
        for (const name of Object.keys(item)) {
            if (name === "time_stamp" || name === "id") {
                continue;
            }
            seriesDict[name].data.value.push([new Date(item["time_stamp"]), item[name]]);
        }
    })

    return series;
}

/**
 * 更新数据
 * @param {Object} data 实时传回的单条数据
 */
function updateSeries(data) {
    for (const name of Object.keys(data)) {
        if (name === "time_stamp" || name === "id") {
            continue;
        }

        /**
         * 防止重复渲染同一时间戳的数据
         */
        let datetimeA = seriesDict[name].data.value[seriesDict[name].data.value.length - 1][0].getTime();
        let datetimeB = new Date(data["time_stamp"]).getTime();
        if (datetimeA !== datetimeB) {
            seriesDict[name].data.value.shift();
            seriesDict[name].data.value.push([new Date(data["time_stamp"]), data[name]]);
        }
    }
}

export { initSeries, setSeries, updateSeries };
