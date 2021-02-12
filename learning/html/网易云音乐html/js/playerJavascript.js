//
// 查询接口:
//     请求地址: https://autumnfish.cn/search
//     请求方法: get
//     请求参数: 查询的关键字 keywords
//     相应内容: 歌曲的搜索结果
// 歌曲地址获取接口:
//     请求地址: https://autumnfish.cn/song/url
//     请求方法: get
//     请求参数: id 歌曲id
//     相应内容: 歌曲的url地址
// 歌曲封面获取接口:
//     请求地址: https://autumnfish.cn/song/detail
//     请求方法: get
//     请求参数: ids 歌曲id
//     相应内容: 歌曲的详情(包括封面图片)
// 歌曲评论获取:
//     请求地址: https://autumnfish.cn/comment/hot?type=0请求方法: get
//     请求参数: id 歌曲的id,type固定为0
//     相应内容: 歌曲的热门评论
// 歌曲MV地址获取:
//     请求地址: https://autumnfish.cn/mv/url
//     请求方法: get
//     请求参数: id (mv的id 如果为0说明没有mv)
//     响应内容: mv的地址

let playerApplication = new Vue({
    el: '#player',
    data: {
        queryText: "",
        musicList: [],
        audioUrl: "",
        songPicUrl: "",
        commentList: [],
        showShadow: false,
        videoUrl: '',
        isPlaying: false
    },
    methods: {
        queryMusic: function () {
            var urlString = "https://www.autumnfish.cn/search"
            var that = this;
            let keywords = that.queryText;
            // console.log(keywords);
            if (that.queryText !== '') {
                axios.get(urlString + '?keywords=' + keywords).then(
                    function (response) {
                        that.musicList = response.data.result.songs;
                    }, function (error) {
                        console.log(error);
                    }
                )
            }
        },
        playMusic: function (musicId) {
            getMusicUrl = 'https://autumnfish.cn/song/url';
            let that = this;
            axios.get(getMusicUrl + "?id=" + musicId).then(function (response) {
                that.audioUrl = response.data.data[0].url;
            }, function (error) {
                console.log(error);
            })

            getMusicAlbum = 'https://autumnfish.cn/song/detail';
            axios.get(getMusicAlbum + '?ids=' + musicId).then(function (response) {
                that.songPicUrl = response.data.songs[0].al.picUrl
            }, function (error) {
                console.log(error);
            })

            urlIdGetComment = 'https://autumnfish.cn/comment/hot?type=0'
            axios.get(urlIdGetComment + '&id=' + musicId).then(function (response) {
                that.commentList = response.data.hotComments;
            }, function (error) {
                console.log(error);
            })
        },
        showMV: function (MVid) {
            that = this;
            getMvUrl = 'https://autumnfish.cn/mv/url'
            axios.get(getMvUrl + '?id=' + MVid).then(function (response) {
                that.videoUrl = response.data.data.url;
                that.showShadow = true;
            }, function (error) {
                console.log(error);
            })
        },
        startMusic: function () {
        },
        pauseMusic: function () {
        },
        closeMV: function () {
            this.videoUrl = "";
            this.showShadow = false
        }
    }
});
