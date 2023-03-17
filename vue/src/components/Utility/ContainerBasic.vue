<template>
    <div class="rounded-md px-8 py-4 justify-items-center grid grid-cols-1 gap-0 bg-gray-100 border shadow-md">
        <div class=" ">
            <p class="text-2xl py-8 font-bold "><slot name="header"></slot></p>
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: "ContainerBasic",

}
</script>