<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'ExploreButton',
  props: {
    pipeline: { type: Object, required: true },
    isDisabled: { type: Boolean, required: false },
    isTooltipLeft: { type: Boolean, required: false }
  },
  computed: {
    ...mapGetters('plugins', ['getInstalledPlugin']),
    ...mapState('repos', ['models']),
    getExploreModel() {
      let targetModel
      for (const prop in this.models) {
        const model = this.models[prop]
        if (model.plugin_namespace === this.getNamespace) {
          targetModel = model
          break
        }
      }
      return targetModel
    },
    getExtractor() {
      // Split based on '@' profiles convention
      return this.pipeline.extractor.split('@')[0]
    },
    getIsExplorable() {
      return Boolean(this.getExploreModel)
    },
    getNamespace() {
      return this.getInstalledPlugin('extractors', this.getExtractor).namespace
    }
  },
  methods: {
    goToExplore() {
      this.$router.push({
        name: 'explore',
        params: { extractor: this.getExtractor }
      })
    }
  }
}
</script>

<template>
  <button
    class="button is-interactive-primary tooltip"
    :class="{ 'is-loading': isDisabled, 'is-tooltip-left': isTooltipLeft }"
    :disabled="isDisabled || !getIsExplorable"
    data-tooltip="Explore dashboards, reports, templates, and more"
    @click="goToExplore"
  >
    <span>Explore</span>
    <span class="icon is-small">
      <font-awesome-icon icon="compass"></font-awesome-icon>
    </span>
  </button>
</template>

<style lang="scss"></style>
