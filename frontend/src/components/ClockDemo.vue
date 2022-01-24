<template>
<p>
    {{this.current_time.hours}}:{{this.current_time.minutes}}:{{this.current_time.seconds}}
    <br />
    {{this.current_time.hours}}:{{this.current_time.minutes}}:{{this.current_time.seconds}}
</p>
</template>

<script>
export default {
    data: function () {
        var date = new Date();
        return {
            current_time: {
                hours: date.getHours(),
                minutes: date.getMinutes(),
                seconds: date.getSeconds(),
            },
        };
    },
    methods: {
        updateTime: function () {
            var date = new Date();
            this.current_time.hours = date.getHours();
            this.current_time.minutes = date.getMinutes();
            this.current_time.seconds = date.getSeconds();
        },
    },
    mounted: function () {
        setInterval(() => {
            this.updateTime();
        }, 1000);
    },
};
</script>

<style scoped>
.chart {
    height: 400px;
}
</style>