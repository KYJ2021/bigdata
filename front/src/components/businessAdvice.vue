<template>
    <div>
        <div class="advice">
            <h2>其他商户怎么做：</h2>
            <el-row :gutter="24" class="cards" style="margin-top: 10px; padding: 10px">
                <el-col :span="8" v-for="(value, key) in currentAd" :key="key">
                    <el-card :body-style="{ padding: '0px' }" shadow="hover" style="height: 60px;margin: 10px">
                        <div style="margin: 15px">
                            <div>{{ key }}
                                <img src="../assets/ok.svg" v-if="value=='True'" style="width: 25px; position: relative; top: 5px; right: 5px; margin-left: 5px">
                                <img src="../assets/cancel.svg" v-if="value=='False'" style="width: 25px; position: relative; top: 5px; right: 5px;margin-left: 5px">
                                <span v-if="value!='True'&&value!='False'" style="margin-left: 20px; color: #999999;">{{value}}</span>
                            </div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <div class="tip">
            <h2>顾客说：</h2>
            <el-row :gutter="24" class="cards" style="margin-top: 10px; padding: 10px">
                <el-col :span="20" v-for="(card, index) in tips" :key="index">
                    <el-card :body-style="{ padding: '0px' }" shadow="hover" @click.native="handleCardClick(card)" style="height: 60px;margin: 10px">
                        <div style="padding: 14px;">
                            <i class="el-icon-user-solid"></i>
                            <a class="card-title" style="margin-left: 10px">{{ card.text }}</a>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import request from "@/utils/request";
export default {
data() {
    return {
        user: JSON.parse(localStorage.getItem("user")),
        categories_array: JSON.parse(localStorage.getItem("user"))['categories'].split(',').map((item) => item.trim()),
        business_id: "",
        city: 'new york',
        searchValue: '',
        tips: [],
        advices: [],
        advice: {},
        currentAd: {},
    };
    },
    created(){
        this.loadAdvice()
        setTimeout(()=>this.loadTip(), 1000);
    },
methods: {
    loadAdvice() {
        request.get("/business/advice", {
            params: {
                categories_array: JSON.stringify(this.categories_array)
            }
        }).then(res => {
            this.advices = res
            this.advices = this.advices.map(item => JSON.parse(item.attributes))
            //去重复的字典项
            this.advice = this.advices.reduce(
                (accumulator, currentValue) => {
                    return Object.assign(accumulator, currentValue);
                    }, {});
            //去除嵌套字典
            this.currentAd = Object.keys(this.advice).filter(key => {
              return !(/^\{.*\}$/.test(this.advice[key]));
            }).reduce((accumulator, currentValue) => {
              accumulator[currentValue] = this.advice[currentValue];
              return accumulator;
            }, {});
            console.log(this.currentAd)
        })
    },
    loadTip(){
        request.get("/business/tip",{
            params: {
                business_id: this.user.id
            }
        }).then(res =>{
            this.tips=res
        })
    },
},
};
</script>
<style scoped>

</style>