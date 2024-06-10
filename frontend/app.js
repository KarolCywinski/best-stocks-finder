const app = Vue.createApp({
    data() {
        return {
            selectedTimeFrame: null,
            shortSell: false,
            timeFrames: [],
            bestStocks: [],
            dataFetched: false
        }
    },
    computed: {
        // column names for the table with the best stocks
        colNames() {
            // get column names from the first best stock object if there is any
            if(this.bestStocks.length > 0) {
                return Object.keys(this.bestStocks[0]);
            }
            else {
                return [];
            }
        },
        // check if all parameters have values, if so, call the best stocks api
        parametersReady() {
            if(this.selectedTimeFrame != null && this.shortSell != null) {
                this.getBestStocks();
                return true;
            }
            return false;
        }
    },
    methods: {
        // list of the best stocks
        getBestStocks() {
            // make api call to fetch the best stocks
            this.dataFetched = false;
            axios
                .get('http://127.0.0.1:8000/get-best-stocks', {
                    params: {
                        short_sell: this.shortSell,
                        time_frame: this.selectedTimeFrame
                    }
                })
                .then(response => {
                        this.bestStocks = response.data;
                        this.dataFetched = true;
                })
        }
    },
    mounted() {
        // make api call to fetch available time frames
        axios
            .get('http://127.0.0.1:8000/get-possible-time-frames')
            .then(response => {
                this.timeFrames = response.data;
            })
    }
});
app.mount('#app');