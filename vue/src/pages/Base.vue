<template>
     <div class="h-screen w-screen flex pt-12 ">
        <div class="flex-grow"></div>
        <router-view></router-view>
        <div class="flex-grow"></div>
    </div>
</template>

<script>
export default {
    name: "Base",

    props: {},

    data: function data() {
        return {};
    },

    mounted() {},

    methods: {},
};
</script>
