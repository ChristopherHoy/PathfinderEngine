<template>
        <div class="h-screen w-screen flex pt-12 ">
            <div class="flex-grow"></div>
            <div class="rounded-md p-8">
                <div class=" flex items-center">
                    <div class="flex-grow"></div>
                        <img src="src/assets/goblin.png"/>
                    <div class="flex-grow"></div>
                </div>

                <div class="py-12 flex">
                    <div class="flex-grow"></div>
                    <p class="text-4xl font-bold"> "Let's do this thing!"</p>
                    <div class="flex-grow"></div>
                </div>
                

                <div class="md:grid-cols-2 grid gap-4 grid-cols-1">
                    <div class=" rounded-md px-8 py-4 justify-items-center grid grid-cols-1 gap-0 bg-gray-100 border shadow-md " >
                        <p class="text-2xl py-8 font-bold ">Player Area</p>
                        <div class="grid-cols-2 grid gap-4 text-base">
                            <div class="bg-white border-2 rounded-md p-4 grid grid-cols-1 gap-4 justify-items-center transition ease-in-out hover:scale-110 duration-200 hover:shadow-lg cursor-pointer" @click="createCharacter">
                                <Icon icon="user-plus" viewBox="0 0 24 24" class="h-8 w-8"></Icon>
                                <p class="text-center">Create Character</p>
                            </div>
                            <div class="bg-white  border-2 rounded-md p-4 grid grid-cols-1 gap-4 justify-items-center transition ease-in-out hover:scale-110 duration-200 hover:shadow-lg cursor-pointer" @click="selectCharacter">
                                <Icon icon="user-group" viewBox="0 0 24 24" class="h-8 w-8"></Icon>
                                <p class="text-center">Select Character</p>
                            </div>
                        </div>
                    </div>
                    <div class="rounded-md px-8 py-4 justify-items-center grid grid-cols-1 gap-0 bg-gray-100 shadow-md border">
                        <p class="text-2xl py-8 font-bold">Game Zone</p>
                        <div class="grid-cols-2 grid gap-4 text-base">
                            <div class="bg-white border-2 rounded-md p-4 grid grid-cols-1 gap-4 justify-items-center transition ease-in-out hover:scale-110 duration-200 hover:shadow-lg cursor-pointer" @click="buildCampaign">
                                <Icon icon="tools" viewBox="0 0 24 24" class="h-8 w-8"></Icon>
                                <p class="text-center">Build Campaign</p>
                            </div>
                            <div class="bg-white border-2 rounded-md p-4 grid grid-cols-1 gap-4 justify-items-center transition ease-in-out hover:scale-110 duration-200 hover:shadow-lg cursor-pointer" @click="selectCampaign">
                                <Icon icon="globe" viewBox="0 0 24 24" class="h-8 w-8"></Icon>
                                <p class="text-center">Select Campaign</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex-grow"></div>
        </div>
</template>

<script>
import Icon from "../components/Utility/Icon.vue"
export default {
    
    name: "Choices",
    components: {
        Icon
    },

    methods: {
        createCharacter() {
            this.$router.push("create-character");
        },

        selectCharacter() {
            console.log("Select Character")
        },

        buildCampaign() {
            console.log("Build Campaign")
        },

        selectCampaign() {
            console.log("Select Campaign")
        }
    }
}
</script>

<style scoped>
    .bg-img {
        background-image: url('src/assets/kraken_battle.jpeg');
        background-size: cover;
        background-position: center
    }
    .glass{
        background-color: rgba(0, 0, 0, 0.17);  
        backdrop-filter: blur(15px);
    }
</style>
  