<template>
  <div>
    <v-text-field
      v-model="interview.title"
      :counter="10"
      label="面试名称"
      required
    ></v-text-field>
    <v-text-field
      v-model="interview.description"
      :counter="50"
      label="描述该面试信息"
      required
    ></v-text-field>
    <v-checkbox
      v-model="interview.edit_finish"
      label="是否完成编辑"
    ></v-checkbox>
    <v-checkbox v-model="interview.is_public" label="是否对外公布"></v-checkbox>
    <v-select
      :items="memberships"
      v-model="interview.out_state"
      item-text="name"
      item-value="url"
    ></v-select>
  </div>
</template>

<script>
export default {
  props: ["interview"],
  computed: {
    memberships() {
      return this.$store.state.memberships;
    }
  }
};
</script>

<style></style>
