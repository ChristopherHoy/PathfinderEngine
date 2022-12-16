<template>
    <div v-for="(item, index) of config.fields" :key="index">
        <TextField v-if="item.type === 'TextField'" :label="item.label" :value="item.default" v-model="item.value" />
    </div>
</template>

<script>
import TextField from "./TextField.vue";
export default {
    name: "Form",

    components: { TextField },

    props: {
        config: {
            type: Object,
            default: () => {
                return { fields: [] };
            },
        },
    },

    data: function data() {
        return {};
    },

    mounted() {},

    methods: {},
};
</script>
